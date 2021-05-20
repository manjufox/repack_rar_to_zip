@echo off
SET INPUTSTR=
SET /P INPUTSTR="input path:"
python repack.py repack_all %INPUTSTR%