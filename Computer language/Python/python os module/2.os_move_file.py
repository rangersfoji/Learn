import os
import shutil

def move_file(file_path,destination_path,lis):
    lis = list(lis)
    before = os.getcwdb().decode('utf-8')
    os.chdir(file_path)
    for file in lis:
        start = os.path.join(file_path,file)
        end = destination_path
        shutil.move(start,end)
    os.chdir(before)
        

# start program
before = os.getcwdb().decode('utf-8')
os.chdir('F:/Desktop/test/')
before_list = os.listdir()


# dowdload files and folder
os.mkdir('demo')
with open('demo.txt','w') as f:
    pass

os.chdir(before)

# after download get what we downloaded
before = os.getcwdb().decode('utf-8')
os.chdir('F:/Desktop/test/')
after_list = os.listdir()
download_list = list(set(after_list).difference(set(before_list)))
os.chdir(before)


move_file('F:/Desktop/test/','F:/Desktop/',download_list)


