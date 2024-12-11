import os
  
# Folder Path
path = os.getcwd()+"/req/"
os.chdir(path)

def read_text_file(file_path):
    with open(file_path, 'r') as f:
        print(f.read())
  
def sorter(file):
    lists = []
    with open(file, "r") as fr:
        for i in fr.readlines():
            lists.append(i)
        fr.close()


    with open(file, "w") as fs:
        lists.sort(key=len)
        for i in lists:
            fs.write(i)
        fs.close()
    lists = None
        
        
for file in os.listdir():
    if file.endswith(".txt"):
        file_path = f"{path}/{file}"
        sorter(file_path)
        read_text_file(file_path)
        
        

