#!/usr/bin/env python3
"""Assemble the revised cover, unchanged parent body and new Appendix I.

Requires PyMuPDF. Compile report/cover.tex and report/prism_addendum.tex first.
"""
from pathlib import Path
import json,hashlib
import fitz
ROOT=Path(__file__).resolve().parents[1]

def assemble() -> dict:
    base=fitz.open(ROOT/'baseline/Unified_Field_Theory_V2_1_0.pdf')
    cover=fitz.open(ROOT/'report/cover.pdf')
    addon=fitz.open(ROOT/'report/prism_addendum.pdf')
    if len(base)!=48 or len(cover)!=1:raise ValueError('Unexpected parent/cover page count')
    out=fitz.open();out.insert_pdf(cover);out.insert_pdf(base,from_page=1,to_page=47);out.insert_pdf(addon)
    toc=[[1,'V2.1.1 release: UU ID Prism',1]]+base.get_toc()
    toc += [[level,title,48+page] for level,title,page in addon.get_toc()]
    out.set_toc(toc)
    out.set_metadata({'title':'Tom Klootwijk — Unified Field Theory V2.1.1: UU ID Prism',
        'author':'Tom Klootwijk','subject':'Rainbow facets, holder-scoped data migration and a personal data passport',
        'keywords':'UU ID, Prism, seven bands, 35 facets, data provenance, personal data passport, V2.1.1',
        'creator':'LaTeX and PyMuPDF','producer':'UU ID Prism corpus edition 2.1.1'})
    out.set_page_labels([{'startpage':0,'prefix':'Cover'},{'startpage':1,'style':'r','firstpagenum':1},
                         {'startpage':3,'style':'D','firstpagenum':1}])
    target=ROOT/'report/Tom_Klootwijk_Unified_Field_Theory_V2_1_1.pdf'
    out.save(target,garbage=4,deflate=True);out.close()
    check=fitz.open(target)
    # Exact raster equality verifies parent-body preservation, beyond text equality.
    preserved=[]
    for i in range(1,48):
        x=base[i].get_pixmap(matrix=fitz.Matrix(1,1),alpha=False)
        y=check[i].get_pixmap(matrix=fitz.Matrix(1,1),alpha=False)
        same=x.samples==y.samples and x.width==y.width and x.height==y.height
        if not same:raise ValueError(f'Parent body changed at physical page {i+1}')
        preserved.append(i+1)
    text_ok=all(base[i].get_text()==check[i].get_text() for i in range(1,48))
    if not text_ok:raise ValueError('Parent body text differs')
    result={'integrated_pdf_pages':len(check),'addendum_pages':len(addon),'addendum_first_physical_page':49,
            'unchanged_parent_body_pages':preserved,'parent_body_raster_equality':True,'parent_body_text_equality':True,
            'pdf_sha256':hashlib.sha256(target.read_bytes()).hexdigest()}
    (ROOT/'verification/pdf_assembly.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2));return result
if __name__=='__main__':assemble()
