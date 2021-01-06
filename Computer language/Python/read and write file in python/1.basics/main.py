# open method (not professional and good way)
'''
f = open('test.txt','r') # different dir , then use path
                         # default 'r' mode if you don't write open('test.txt')

    # r = read
    # w = write (overrite)
    # r+ = read and write
    # a = append (add write)
print(f.name)  # ot = test.txt
print(f.mode) # ot = r
f.close()
'''
# in upper method you have to close file 
# if you forget to close then it would be problem (data leak,error,memory error)
# solution : use context manager


#context manager
# in this method you don't need to close it it's automaticaly close the file

# read file
'''
with open('test.txt','r') as f :
    print(f.name)
    print(f.mode)

    # read
    f_contents = f.read()
    print(f_contents)   # ot = all file text

    # if you have small file this is what you do
    # but what if you have too huge file and you don't want to load all content  into one memory
    
    
    # use readlines()
    f_content = f.readlines()
    print(f_content) # ot = give a list of line

    # readline()
    f_content = f.readline()
    print(f_content,end = '') # ot = first line

    f_content = f.readline()
    print(f_content,end = '') # ot = second line

    # you can use either read or readlines or readline in one file


    # solution of don't want to read at one memory
    for i in f:
        print(i,end='')


    # if you want to read 10 alphabate in one time
    f_content = f.read(10)
    print(f_content,end='') # ot = first 10 alphabate

    f_content = f.read(10)
    print(f_content,end='') # ot = second 10 alphabate

    f_content = f.read(10)
    print(f_content,end='') # ot = three 10 alphabate
    # if this read funtion read all
    # and if you will try again nothing will happen
    # because that read funtion return empty string and print

    # use :
    siz = 5
        
    f_content = f.read(siz)

    while len(f_content) > 0:
        print(f_content,end='')
        f_content = f.read(siz)


    # tell method (tell's what's the last charater you read )
    print(f.tell())


    # seek method (that set last read charater at position use pass)
    f.seek(0)

'''


# write file
# 'w' : if file don't exists then it creat it
# and if file does exists then it overwrite it
'''
with open('test2.txt','w')as f:
    f.write('Test')
    f.write('Test') # ot = TestTest

    f.write('22')
    f.seek(0)
    f.write('1') # ot = 12 
                 # because it overwrite it at that position
'''

# read and write file
'''
with open('test.txt','r') as rf:
    with open('test3.txt','w') as wf:
        for line in rf:
            wf.write(line)
'''
# we copied file

# what if we want to copy image 
# in image we have to work with binory codes
'''
with open('img.jfif','rb') as rf: # here rb for read binary
    with open('img_copy.jfif','wb') as wf:
        for line in rf:
            wf.write(line)
'''
# you can do this way as well: (maybe fast and stable)
'''
with open('img.jfif','rb') as rf:
    with open('img_copy.jfif','wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)

        while len(rf_chunk)>0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
'''
        




