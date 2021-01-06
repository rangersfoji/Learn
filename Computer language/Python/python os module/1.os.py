import os
import shutil
import time

# 1 : get current dir path
# before = os.getcwd()
    # inbyte and convert in str
# before = os.getcwdb().decode('utf-8')

# 2 : change dir
# os.chdir('F:/Desktop')
# os.chdir(before)

# 3 : get list of files and folders in current dir
# ls = os.listdir()
# print(ls)

# 4 : create folder
# os.mkdir('demo') # can make one folder
# os.makedirs('demo/1/2/3/4') # can make one folder with subfolders

# if you want to create multiple folders in same direcotry
# solution use for loop mkdir
# and if you want to create folders with subfolder
# solution use for loop with makedirs

# 5 : create file
# use with open(path,'w') as f:
#   pass


# 6 : delete folder
    # file : os.remove(path)
    # empty folder : os.rmdir(path)
    # full folder : shutil.rmtree(path)

# 7 : rename folder
    # old = os.rename
    # new = os.renames

    # renames works like bash mv
    # renames('old name','new name')  # rename folder or file
    # renames('file/folder name','move path')

# 8 : get all info about folder (important you can do so many thing)

# for current_path,folder_names,file_names in os.walk(path):
#     print('path : ',current_path)
#     print('folders : ',folder_names)
#     print('files : ',file_names)
#     print()


# 9 : get environment variable details and other things

    # 1 : join
    # print(os.environ.get('Home')) # ot = C:\Users\Karan
    # now if i want to create 'test.txt' file in this directory
    # root = os.environ.get('Home')
    # file = 'text.txt'
    # file_path = os.path.join(root,file)
    # print(file_path) # ot = C:\Users\Karan\text.txt

    # create file
    # with open(file_path,'w') as f:
        # pass


    # 2 : basename (gives path's last folder or file)
    # a = os.path.basename(os.environ.get('Home')+'/text.py')
    # print(a) # ot = test.py / if os.environ.get('Home') then ot = Karan


    # 3 : dirname (gives path with out last folder or file)
    # a = os.path.dirname(os.environ.get('Home'))
    # print(a) # ot = C:\Users  but not Karan 

    # 4 : exists (check path exits )
    # print(os.path.exists('F:/text.txt')) # ot = False

    # 5 : isdir (# some times file don't have extention like .py , .txt)
    #              if path = C:/Users/Karan/text
    #              if you want to check that is text is folder then
    # print(os.path.isdir('C:/Users/Karan/text'))  if false means file otherwise folder

    # 6 : isfile (same as isdir)

    # 7 : splitext 
    # path = '/test/demo.txt'
    # print(os.path.splitext(path)) ot = ('/test/demo', '.txt')

    
