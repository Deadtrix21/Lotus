import os, re, shutil
  
# Folder Path
path = os.getcwd()
os.chdir(path)
pattern = "__pycache__"
directList = list()


def remacthcode(string):
    res = re.search(pattern, string)
    if res:
        return True
    else:
        return False 

for i in os.walk(path):
    dir, *contents = i
    if remacthcode(dir):
        directList.append(dir)



for i in directList:
    print(i)
    if remacthcode(i):
        try:
            shutil.rmtree(i)
        except Exception as E:
            pass