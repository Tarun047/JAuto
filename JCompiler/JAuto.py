import tempfile
import subprocess
import sys
import os

with tempfile.TemporaryDirectory(prefix = sys.argv[1],dir=os.getcwd()) as temp:
    if len(sys.argv)==1:
        print("Please Specify FileName")
        sys.exit(0)
    p = subprocess.Popen('javac -d '+temp+' '+sys.argv[1],shell=True)
    
    mainclassname = input('Please Enter: Main Class Name:(leave blank for default filename)\n')
    if mainclassname == '':
        mainclassname=os.path.splitext(sys.argv[1])[0]
    subprocess.call('java '+mainclassname,shell=True,cwd=temp)
    try:
        os.remove(temp)
    except:
        sys.exit(0)
