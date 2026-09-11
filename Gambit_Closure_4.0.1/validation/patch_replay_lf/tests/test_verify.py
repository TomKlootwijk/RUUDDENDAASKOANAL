"""Coordinator regressions use isolated synthetic outputs, not kernel evidence."""
import contextlib
import hashlib
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
import verify


class VerificationWorkflowTests(unittest.TestCase):
    def coordinator(self,flags,formal_status='PASS',launch_error=False):
        with tempfile.TemporaryDirectory() as temporary:
            root=Path(temporary);out=root/'result';(root/'assets').mkdir()
            asset=root/'assets/micro_xy.gblut';asset.write_bytes(b'fixture')
            (root/'SHA256SUMS.txt').write_text(hashlib.sha256(asset.read_bytes()).hexdigest()+'  assets/micro_xy.gblut\n')
            payload={'initial.gbc':b'initial','final.gbc':b'complete','words.bin':b'0'*28+b'abcdef','summary.csv':b'csv','counts.bin':b'counts'}
            (root/'assets/closure_goldens.json').write_text(json.dumps({'cases':{'micro_xy':{
                'asset':asset.name,'steps':64,'files':{name:hashlib.sha256(data).hexdigest() for name,data in payload.items()}}}}))

            def write_output(dest):
                dest.mkdir(parents=True)
                for name,data in payload.items():
                    if name=='words.bin' and dest.name=='split_first':data=b'0'*28+b'abc'
                    if name=='words.bin' and dest.name=='split_second':data=b'0'*28+b'def'
                    (dest/name).write_bytes(data)

            def run(cmd,**kwargs):
                if launch_error:raise OSError('synthetic executable launch failure')
                code=0
                if 'tools/check_formal.py' in cmd:
                    dest=Path(cmd[cmd.index('--out')+1]);dest.mkdir()
                    (dest/'report.json').write_text(json.dumps({'status':formal_status,'targets':[]}))
                    code={'PASS':0,'BLOCKED':2,'FAIL':1}[formal_status]
                elif '-DGAMBIT_ENABLE_CUDA=ON' in cmd:code=9
                elif '--out' in cmd:
                    dest=Path(cmd[cmd.index('--out')+1])
                    if dest.name.startswith('negative_'):code=1
                    else:write_output(dest)
                return subprocess.CompletedProcess(cmd,code)

            with contextlib.ExitStack() as stack:
                stack.enter_context(patch.object(verify,'ROOT',root))
                stack.enter_context(patch.object(sys,'argv',['verify.py','--out',str(out)]+flags))
                stack.enter_context(patch.object(verify,'tool_path',side_effect=lambda name:root/(name+'.exe')))
                stack.enter_context(patch.object(verify,'exe',return_value=root/'gambit.exe'))
                stack.enter_context(patch.object(verify.subprocess,'run',side_effect=run))
                stack.enter_context(patch.object(verify,'decode_asset',return_value=()))
                stack.enter_context(patch.object(verify,'Reference'))
                stack.enter_context(patch.object(verify,'python_run',side_effect=lambda engine,dest,steps:write_output(dest)))
                stack.enter_context(patch.object(verify,'audit',return_value={}))
                stack.enter_context(contextlib.redirect_stdout(io.StringIO()))
                code=verify.main()
            report=json.loads((out/'verification.json').read_text())
            log_text={path.name:path.read_text() for path in (out/'logs').glob('*.txt')}
            return code,report,log_text

    def test_formal_blocked_is_recorded_with_requested_later_gates(self):
        code,report,_=self.coordinator(['--hardware','--formal','--sanitizers','--profile'],formal_status='BLOCKED')
        self.assertEqual(code,2)
        self.assertEqual(report['status'],'BLOCKED')
        self.assertEqual(report['cpu'],'PASS')
        self.assertEqual(report['formal'],'BLOCKED')
        self.assertEqual(report['failed_gate'],'formal')
        for gate in ['gpu','sanitizers','profile']:
            self.assertTrue(report['requested'][gate])
            self.assertEqual(report[gate],'NOT_RUN')
        self.assertEqual(report['commands'][-1]['returncode'],2)

    def test_cuda_toolset_is_explicit_and_cpu_configuration_is_unchanged(self):
        code,report,_=self.coordinator(['--hardware','--formal','--cmake-cuda-toolset','cuda=12.8'])
        self.assertEqual(code,1)
        self.assertEqual(report['cpu'],'PASS')
        self.assertEqual(report['formal'],'PASS')
        self.assertEqual(report['gpu'],'FAIL')
        self.assertEqual(report['failed_gate'],'gpu')
        commands={command['log']:command for command in report['commands']}
        self.assertNotIn('-T',commands['configure.txt']['argv'])
        self.assertEqual(commands['cuda_configure.txt']['argv'][-2:],['-T','cuda=12.8'])
        self.assertEqual(commands['cuda_configure.txt']['returncode'],9)

    def test_failed_process_launch_preserves_command_and_error_log(self):
        code,report,logs=self.coordinator(['--cpu-only','--formal'],launch_error=True)
        self.assertEqual(code,2)
        self.assertEqual(report['cpu'],'BLOCKED')
        self.assertEqual(report['formal'],'NOT_RUN')
        self.assertIsNone(report['commands'][0]['returncode'])
        self.assertIn('synthetic executable launch failure',report['commands'][0]['launch_error'])
        self.assertIn('synthetic executable launch failure',logs['configure.txt'])

    @unittest.skipUnless(os.name=='nt','Windows batch launcher regression')
    def test_nvidia_forwarding_launcher_resolves_without_shell(self):
        with tempfile.TemporaryDirectory(prefix='NVIDIA tools ') as temporary:
            root=Path(temporary);(root/'bin').mkdir();(root/'compute-sanitizer').mkdir()
            direct=root/'compute-sanitizer/compute-sanitizer.exe';direct.touch()
            launcher=root/'bin/compute-sanitizer.bat'
            launcher.write_text('@echo off\n"%~dp0\\..\\compute-sanitizer\\compute-sanitizer.exe" %*\n')
            with patch.object(verify.shutil,'which',return_value=str(launcher)):
                self.assertEqual(verify.tool_path('compute-sanitizer'),direct.resolve())
            launcher.write_text('@echo off\nset IMPORTANT_SETUP=1\n"%~dp0\\..\\compute-sanitizer\\compute-sanitizer.exe" %*\n')
            with patch.object(verify.shutil,'which',return_value=str(launcher)):
                with self.assertRaises(verify.Blocked):verify.tool_path('compute-sanitizer')


if __name__=='__main__':unittest.main()
