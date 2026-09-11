#!/usr/bin/env python3
"""Assemble editable Markdown/LaTeX and PDF. Requires pandoc and pdflatex."""
from __future__ import annotations
import re, shutil, subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DOCS=['RELEASE.md','MIGRATION.md','MODEL_AND_PROOFS.md','NATIVE_IMPLEMENTATION.md',
      'BINARY_FORMATS.md','DELIVERY_EVIDENCE.md','CODEX_VERIFY.md','REFERENCES.md']

def main():
    for program in ('pandoc','pdflatex'):
        if not shutil.which(program):
            raise SystemExit(f'{program} is required for manuscript reproduction, not for the native runtime')
    parts=[]
    for name in DOCS:
        text=(ROOT/'docs'/name).read_text()
        text=re.sub(r'(?m)^## \d+\. ', '## ', text)
        # The model document's second heading line is useful metadata but the title is enough here.
        if parts:parts.append('\\clearpage\n\n')
        if name=='REFERENCES.md':
            text='\\begingroup\\small\n\n'+text+'\n\n\\endgroup\n'
        parts.append(text+'\n')
    md=ROOT/'manuscript/Gambit_CUDA_3.1.md';md.write_text('\n'.join(parts))
    fragment=ROOT/'manuscript/body.tex'
    subprocess.run(['pandoc',str(md),'-f','markdown+tex_math_dollars+raw_tex','-t','latex',
                    '--no-highlight','--wrap=none','-o',str(fragment)],cwd=ROOT,check=True)
    body=fragment.read_text()
    # Long literal filenames/paths remain readable with TeX's URL line-breaking machinery.
    def break_path(match):
        raw=match.group(1).replace('\\_','_')
        if re.fullmatch(r'[A-Za-z0-9._/\-]+',raw) and ('/' in raw or '_' in raw):
            return '\\path{'+raw+'}'
        return match.group(0)
    body=re.sub(r'\\texttt\{([^{}]*)\}',break_path,body)
    body=body.replace('\\begin{verbatim}', '\\par\n\\begin{minipage}{\\linewidth}\n\\begin{verbatim}')
    body=body.replace('\\end{verbatim}', '\\end{verbatim}\n\\end{minipage}\n\\par')
    tex=ROOT/'manuscript/Gambit_CUDA_3.1.tex'
    tex.write_text((ROOT/'manuscript/preamble.tex').read_text()+body+'\n\\end{document}\n')
    build=ROOT/'manuscript/build';build.mkdir(exist_ok=True)
    for _ in range(3):
        result=subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error',
                               '-output-directory',str(build),str(tex)],cwd=ROOT,
                              stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        (build/'console.txt').write_text(result.stdout)
        if result.returncode:
            print(result.stdout[-6000:]);raise SystemExit(result.returncode)
    destination=ROOT/'Tom_Klootwijk_Gambit_CUDA_Kernel_3.1.pdf'
    shutil.copy2(build/'Gambit_CUDA_3.1.pdf',destination)
    print(destination)
if __name__=='__main__':main()
