#!/usr/bin/env python3
"""Index an explicitly selected local folder. No upload, sensor access or payload copy.

Output contains filenames, byte sizes and hashes. Keep it private. Symlinks are
skipped; a changed file or an exceeded byte budget is reported instead of indexed.
"""
from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json,os,stat,sys

def inventory(root: Path,max_bytes: int=100*1024*1024,excluded: Path|None=None) -> dict:
    root=root.resolve(strict=True)
    if not root.is_dir() or max_bytes<1:raise ValueError('A folder and positive per-file budget are required')
    files=[];skipped=[]
    for folder,dirs,names in os.walk(root,followlinks=False):
        dirs[:]=sorted(d for d in dirs if not (Path(folder)/d).is_symlink())
        for name in sorted(names):
            p=Path(folder)/name
            rel=p.relative_to(root).as_posix()
            if excluded is not None and p.resolve()==excluded.resolve():continue
            if p.is_symlink():skipped.append({'path':rel,'reason':'symlink'});continue
            try:
                flags=os.O_RDONLY | getattr(os,'O_NOFOLLOW',0) | getattr(os,'O_NONBLOCK',0)
                fd=os.open(p,flags)
                with os.fdopen(fd,'rb') as f:
                    before=os.fstat(f.fileno())
                    if not stat.S_ISREG(before.st_mode):raise ValueError('not_regular_file')
                    if before.st_size>max_bytes:raise ValueError('byte_budget')
                    h=hashlib.sha256();total=0
                    while chunk:=f.read(1024*1024):
                        total+=len(chunk)
                        if total>max_bytes:raise ValueError('byte_budget')
                        h.update(chunk)
                    after=os.fstat(f.fileno())
                    if (before.st_size,before.st_mtime_ns)!=(after.st_size,after.st_mtime_ns) or total!=after.st_size:
                        raise ValueError('changed_during_read')
                files.append({'relative_path':rel,'byte_size':total,'payload_sha256':h.hexdigest(),'facet_id':None})
            except (OSError,ValueError) as exc:skipped.append({'path':rel,'reason':str(exc)})
    return {'format':'UU-PRISM-INVENTORY','version':'2.1.1','root_label':root.name,
      'created_at':datetime.now(timezone.utc).isoformat().replace('+00:00','Z'),
      'files':files,'skipped':skipped,'file_count':len(files),'total_bytes':sum(x['byte_size'] for x in files),
      'migration_mode':'index-and-link; original files remain in place'}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--max-file-bytes',type=int,default=100*1024*1024)
    a=p.parse_args()
    try:
        result=inventory(a.root,a.max_file_bytes,a.out);a.out.parent.mkdir(parents=True,exist_ok=True)
        a.out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
        print(f'Indexed {result["file_count"]} files; {len(result["skipped"])} skipped. No files uploaded or copied.')
    except (ValueError,OSError) as exc:print(str(exc),file=sys.stderr);sys.exit(1)
