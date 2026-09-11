#!/usr/bin/env python3
"""Build editable LaTeX and PDF from Markdown; requires installed Pandoc and pdfLaTeX.
Run from any directory. No downloads. Existing PDF is replaced deliberately.
Figures are included as frozen PDFs; optional make_figures.py regenerates them.
"""
from pathlib import Path
import argparse,os,shutil,subprocess,sys,re
ROOT=Path(__file__).resolve().parents[1]
NAME='Tom_Klootwijk_Gambit_Closed_Engine_4.0'
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--build-dir',type=Path,default=ROOT/'local_verification/pdf_build');a=ap.parse_args()
    for tool in ['pandoc','pdflatex']:
        if not shutil.which(tool):ap.error('Required installed tool absent: '+tool)
    build=a.build_dir.resolve();build.mkdir(parents=True,exist_ok=True)
    body=subprocess.check_output(['pandoc','-f','markdown','-t','latex','--no-highlight',str(ROOT/'manuscript/Closure_4.0.md')],text=True)
    # Major sections start consistently; subordinate proofs flow normally.
    body=re.sub(r'\\section\{([^}]+)\}', lambda m: ('\\clearpage\n' if m.group(1).startswith(('Unified Closure','Supporting proof','References and source')) else '') + m.group(0), body, flags=re.S)
    body=body.replace(r'\texttt{provenance/engineering\_3.1\_original.zip}',r'\path{provenance/engineering_3.1_original.zip}')
    body=body.replace(r'\texttt{provenance/closure\_corpus\_original.pdf}',r'\path{provenance/closure_corpus_original.pdf}')
    pre=(ROOT/'manuscript/preamble.tex').read_text()
    tex=ROOT/'manuscript'/f'{NAME}.tex';tex.write_text(pre+'\n'+body+'\n\\end{document}\n')
    env=dict(os.environ,SOURCE_DATE_EPOCH='1789084800',FORCE_SOURCE_DATE='1')
    for i in range(3):
        with (build/f'pass_{i+1}.txt').open('w') as log:
            subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error','-file-line-error','-output-directory',str(build),str(tex)],cwd=ROOT,stdout=log,stderr=subprocess.STDOUT,env=env,check=True)
    dest=ROOT/f'{NAME}.pdf';shutil.copyfile(build/f'{NAME}.pdf',dest)
    print(dest)
if __name__=='__main__':main()
