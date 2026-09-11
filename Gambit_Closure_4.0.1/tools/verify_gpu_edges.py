#!/usr/bin/env python3
"""Additional bounded CUDA regressions; no installs, network or golden updates.

The normal coordinator covers frozen trajectories. This script covers its missing
block-64 option, feedback-off texture/global execution and rejection/error paths.
Optional diagnostics compile explicitly fault-injected copies under --out only.
"""
from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

from audit_trace import audit
from reference import Reference, decode_asset, run as python_run

ROOT = Path(__file__).resolve().parents[1]
FILES = ("initial.gbc", "final.gbc", "words.bin", "summary.csv", "counts.bin")


def digest(path):
    with Path(path).open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cpu", type=Path, required=True)
    parser.add_argument("--gpu", type=Path, required=True)
    parser.add_argument("--contract", type=Path, help="Built gambit_cuda_contract executable")
    parser.add_argument("--out", type=Path, required=True, help="Unused output directory")
    parser.add_argument("--diagnostics", action="store_true", help="Compile isolated step-3 cell/clock faults")
    parser.add_argument("--nvcc", type=Path)
    parser.add_argument("--core-lib", type=Path, help="Release closure_core library for fault builds")
    parser.add_argument("--host-compiler", type=Path, help="NVCC -ccbin compiler or directory")
    args = parser.parse_args()
    args.cpu, args.gpu, args.out = args.cpu.resolve(), args.gpu.resolve(), args.out.resolve()
    if args.out.exists():
        parser.error("--out must be an unused path")
    for label, path in (("cpu", args.cpu), ("gpu", args.gpu), ("contract", args.contract)):
        if path is not None and not path.is_file():
            parser.error(f"--{label} executable is absent: {path}")
    if args.diagnostics and (args.core_lib is None or not args.core_lib.is_file()):
        parser.error("--diagnostics requires an existing --core-lib")
    nvcc = args.nvcc or shutil.which("nvcc")
    if args.diagnostics and not nvcc:
        parser.error("--diagnostics requires an available NVCC compiler")

    args.out.mkdir(parents=True)
    logs = args.out / "logs"
    logs.mkdir()
    source = ROOT / "src/cuda.cu"
    protected = (source, ROOT / "assets/closure_goldens.json", ROOT / "SHA256SUMS.txt")
    protected_before = {str(path): digest(path) for path in protected}
    report = {
        "schema": "gambit-cuda-edge-verification-4.0.1",
        "status": "RUNNING",
        "started_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "scope": "Bounded additional regressions, not whole-program proof",
        "production_source_sha256": digest(source),
        "cpu_executable": {"path": str(args.cpu), "sha256": digest(args.cpu)},
        "gpu_executable": {"path": str(args.gpu), "sha256": digest(args.gpu)},
        "commands": [],
        "cases": {},
        "diagnostics": "NOT_RUN",
    }

    def save():
        (args.out / "verification.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    def invoke(command, tag, *, expected_code=0, expected_text=None, env=None):
        command = [str(part) for part in command]
        print("+", subprocess.list2cmdline(command), flush=True)
        result = subprocess.run(command, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, env=env)
        (logs / (tag + ".txt")).write_bytes(result.stdout)
        output = result.stdout.decode("utf-8", errors="replace")
        item = {"argv": command, "returncode": result.returncode, "expected_returncode": expected_code,
                "log": "logs/" + tag + ".txt"}
        if expected_text is not None:
            item["expected_text"] = expected_text
        if env is not None:
            item["environment_overrides"] = {"CUDA_VISIBLE_DEVICES": env["CUDA_VISIBLE_DEVICES"]}
        report["commands"].append(item)
        save()
        if result.returncode != expected_code:
            raise RuntimeError(f"{tag}: return code {result.returncode}, expected {expected_code}")
        if expected_text is not None and expected_text not in output:
            raise RuntimeError(f"{tag}: expected diagnostic absent")
        if expected_code and "PASS" in output:
            raise RuntimeError(f"{tag}: rejected run printed PASS")
        return output

    def hashes(path):
        return {name: digest(path / name) for name in FILES}

    def same(left, right):
        a, b = hashes(left), hashes(right)
        if a != b:
            raise RuntimeError(f"Five-file conformance failure: {left} vs {right}")
        return a

    def verified_case(tag, path, reference):
        report["cases"][tag] = {"status": "PASS", "five_file_sha256": same(path, reference), "audit": audit(path)}
        save()

    try:
        save()
        report["device"] = json.loads(invoke([args.gpu, "--inspect"], "device"))
        if args.contract:
            invoke([args.contract.resolve()], "cuda_wrapper_contract", expected_text="PASS CUDA wrapper:")
            report["wrapper_contract"] = {"status": "PASS", "sha256": digest(args.contract)}

        # Block 64 is admitted by the CLI but omitted by the original coordinator.
        block_cpu, block_gpu = args.out / "block64_native", args.out / "block64_cuda"
        asset = ROOT / "assets/verify_xy.gblut"
        invoke([args.cpu, "--asset", asset, "--steps", 64, "--out", block_cpu], "block64_native")
        expected = json.loads((ROOT / "assets/closure_goldens.json").read_text())["cases"]["verify_xy"]["files"]
        if hashes(block_cpu) != expected:
            raise RuntimeError("Block-64 native baseline did not match the frozen verify_xy golden")
        invoke([args.gpu, "--asset", asset, "--steps", 64, "--block", 64, "--fetch", "texture", "--out", block_gpu], "block64_cuda")
        verified_case("texture_block64_frozen_golden", block_gpu, block_cpu)

        # Feedback-off has no frozen golden; independent Python supplies a second implementation.
        micro = ROOT / "assets/micro_xy.gblut"
        off_cpu, off_python = args.out / "feedback0_native", args.out / "feedback0_python"
        invoke([args.cpu, "--asset", micro, "--steps", 64, "--feedback", 0, "--out", off_cpu], "feedback0_native")
        python_run(Reference(*decode_asset(micro.read_bytes()), feedback=0), off_python, 64)
        verified_case("feedback0_native_python", off_cpu, off_python)
        for fetch in ("texture", "global"):
            target = args.out / ("feedback0_" + fetch)
            invoke([args.gpu, "--asset", micro, "--steps", 64, "--feedback", 0, "--fetch", fetch, "--block", 256, "--out", target], "feedback0_" + fetch)
            verified_case("feedback0_cuda_" + fetch, target, off_python)

        for tag, extra, message in (
            ("invalid_block31", ["--block", 31], "Invalid run arguments"),
            ("invalid_steps0", ["--steps", 0], "Invalid run arguments"),
            ("invalid_fetch", ["--fetch", "nonsense"], "Invalid run arguments"),
            ("invalid_feedback2", ["--feedback", 2], "Invalid run arguments"),
            ("unsupported_gates", ["--backend", "gates"], "Boolean ALU backend is a CPU conformance oracle, not a CUDA option"),
        ):
            target = args.out / tag
            invoke([args.gpu, "--asset", micro, "--out", target] + extra, tag, expected_code=1, expected_text=message)
            if target.exists():
                raise RuntimeError(tag + ": rejected arguments created an output directory")
            report["cases"][tag] = {"status": "PASS", "rejected_without_output": True}
        target = args.out / "invalid_resume_feedback"
        invoke([args.gpu, "--resume", off_cpu / "final.gbc", "--feedback", 0, "--out", target],
               "invalid_resume_feedback", expected_code=1, expected_text="Invalid run arguments")
        if target.exists():
            raise RuntimeError("Rejected resume feedback created an output directory")
        report["cases"]["invalid_resume_feedback"] = {"status": "PASS", "rejected_without_output": True}

        # Process-local device hiding exercises a real failing wrapped CUDA API call.
        invoke([args.gpu, "--inspect"], "no_visible_device", expected_code=1,
               expected_text="FAIL: cudaGetDeviceProperties(&d,0): ",
               env=dict(os.environ, CUDA_VISIBLE_DEVICES="-1"))
        report["cases"]["no_visible_device"] = {"status": "PASS", "scope": "Process-local CUDA visibility only"}

        if args.diagnostics:
            faults = args.out / "isolated_diagnostic_faults"
            faults.mkdir()
            production = source.read_text(encoding="utf-8")
            needle = "reference.tick();session.tick(state);gambit::compare_states(state.cells,reference.cells,step);"
            if production.count(needle) != 1:
                raise RuntimeError("Production diagnostic site changed; isolated fault insertion requires review")
            diagnostic_results = {}
            for kind, injected, message in (
                ("cell", "if(step==3)state.cells[0].memory^=1u;", "FAIL: CPU/GPU state mismatch at step 3, cell 0"),
                ("clock", "if(step==3)state.clock.phase^=1u;", "FAIL: GPU/native closed-transition mismatch at step 3"),
            ):
                fault_source = faults / (kind + ".cu")
                replacement = "reference.tick();session.tick(state);" + injected + "gambit::compare_states(state.cells,reference.cells,step);"
                fault_source.write_text("// TEST-ONLY fault injection; never a production executable.\n" + production.replace(needle, replacement), encoding="utf-8")
                binary = faults / (kind + (".exe" if os.name == "nt" else ""))
                command = [nvcc, "-std=c++17", "-gencode=arch=compute_120,code=sm_120", "--fmad=false", "-I", ROOT / "include"]
                if os.name == "nt":
                    command += ["-Xcompiler=/MT,/EHsc"]
                if args.host_compiler:
                    command += ["-ccbin", args.host_compiler.resolve()]
                command += [fault_source, args.core_lib.resolve(), "-o", binary]
                invoke(command, "fault_" + kind + "_build")
                target = faults / (kind + "_run")
                invoke([binary, "--asset", micro, "--steps", 8, "--out", target], "fault_" + kind + "_run",
                       expected_code=1, expected_text=message)
                if (target / "final.gbc").exists() or (target / "run.json").exists():
                    raise RuntimeError("Diagnostic failure produced completed-run artifacts")
                if len((target / "summary.csv").read_text().splitlines()) != 4:
                    raise RuntimeError("Diagnostic did not stop after exactly three successful updates")
                diagnostic_results[kind] = {"status": "PASS", "injected_zero_based_tick": 3,
                                            "successful_updates_before_failure": 3, "source_sha256": digest(fault_source),
                                            "binary_sha256": digest(binary), "diagnostic": message}
            report["diagnostics"] = diagnostic_results

        protected_after = {str(path): digest(path) for path in protected}
        if protected_before != protected_after:
            raise RuntimeError("Production source, frozen goldens or release manifest changed during regression run")
        report["protected_files_unchanged"] = protected_after
        report["status"] = "PASS_REQUESTED_SCOPE"
        report["finished_utc"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
        save()
        print("PASS: requested CUDA edge regressions; see", args.out / "verification.json")
        return 0
    except Exception as failure:
        report["status"] = "FAIL"
        report["reason"] = str(failure)
        save()
        print("FAIL:", failure)
        return 1


if __name__ == "__main__":
    sys.exit(main())
