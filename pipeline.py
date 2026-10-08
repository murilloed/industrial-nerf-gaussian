"""Prepare or execute Nerfstudio scene training. Install its environment separately."""
import argparse,subprocess
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--data',required=True);p.add_argument('--method',choices=['nerfacto','splatfacto'],required=True);p.add_argument('--execute',action='store_true');a=p.parse_args()
data=Path(a.data).resolve()
if not (data/'transforms.json').is_file():p.error('Processed scene with transforms.json required')
command=['ns-train',a.method,'--data',str(data)];print(subprocess.list2cmdline(command))
if a.execute:subprocess.run(command,check=True)
