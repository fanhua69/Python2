import os,glob

os.chdir("/Users/fanhua/exer/python")
for file in glob.glob("*.py"):
    print(file)