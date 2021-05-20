import asyncio
import fire
from icecream import ic
import os
from pathlib import Path
import patoolib
from send2trash import send2trash
import shutil

async def repack(path):
    try:
        patoolib.repack_archive(path,path[:-4]+".zip")
    finally:
        delete_file(path)

async def _repack_all(path):
    listdir = list(Path(path).glob("**/*.rar"))
    listdir = map(lambda x:str(x),listdir)
    for p in listdir:
        await repack(p)

def repack_all(path):
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(_repack_all(path))
    finally:
        loop.close()      

async def delete_file(path):
    try:
        send2trash(path)
    except:
        pass  

if __name__ == '__main__':
  fire.Fire()