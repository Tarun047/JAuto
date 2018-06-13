import os
import tempfile
import shutil
from subprocess import check_output
from os.path import basename,normpath,splitext
import sys

base = os.getcwd()
name = basename(normpath(base))
temp = tempfile.mkdtemp(prefix=name,dir=base)
try:
    if len(sys.argv)==1:
        print("Please Specify FileName")
        sys.exit(0)
    check_output('javac -d '+temp+' '+sys.argv[1],shell=True)
    mainclassname = input('Please Enter: Main Class Name:(leave blank for default filename)')
    if mainclassname == '':
        mainclassname=splitext(sys.argv[1])[0]
    
    print(check_output('java '+mainclassname,shell=True,cwd=temp).decode('utf-8'),file=sys.stdout)
finally:
    shutil.rmtree(temp)
