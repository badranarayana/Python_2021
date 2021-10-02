import os

"""
# get the current working directory
dir_name = os.getcwd()
# getting the path from where we run the script, not the location of module stored
print(dir_name)
# ?

# changing current directory
print("-------------------")
dir_name = os.getcwd()   # w -> cd or linux -> pwd
print("Before change")
print(dir_name)
os.chdir(r"files_data")
print("After change directory")
new_path = os.getcwd()
print(os.listdir(new_path))  # windows dir, linux -> ls


# Getting cwd
# change directory
# listdir


print("---------list dir ----------")
#root_dir = r"C:\sers\91901\Desktop\stock_feeds\iles_data"
# List out the content in root dir
content = os.listdir(root_dir)
for file_name in content:
    file_full_path = os.path.join(root_dir, file_name)
    print("--->", file_full_path)
    with open(file_full_path, ) as obj:
        print(obj.read())
    print("*******************************")


# Creating dir
#os.mkdir()
#os.makedirs()

root = r"C:\sers\91901\Desktop\stock_feeds"

folder_path = os.path.join(root, "files_data_new_2")

for path in ['new1', 'new2']:
    os.makedirs(os.path.join(folder_path, path), exist_ok=True)
print(folder_path)

# we can user mkdir()
#os.mkdir(folder_path)

#my_new = os.path.join(folder_path, "new")
#os.mkdir(my_new)
#print("--", os.listdir(folder_path))
#os.makedirs(folder_path)

# os.mkdir() is only used to create single directory,
# it throw an error if any dir doesn't exit in path
# c://user/downloads/new
# if downloads folder not there, then make dir throw an exception like path not found

# os.makedirs(): it will crate tree of directories if not exist already.

#--------------------------------------------------
# how do we check if the path is dir path or file path
my_file_path = os.path.join(folder_path, 'test.txt')
print(my_file_path)
print(os.path.isdir(folder_path))
print(os.path.isfile(my_file_path))

# how do we check if given path exist in computer?
is_path_exits = os.path.exists(my_file_path)
print(is_path_exits)

# Create directory if doesn't exited?
my_new_3 = os.path.join(folder_path, "new3")
if not os.path.exists(my_new_3):
    os.mkdir(my_new_3)


# listing,
# creating dirs,
# checking for file and dir,
# path existed or not

import shutil

# removing file and directories
#os.removedirs(folder_path) # use this id dir is empty (directory)
#shutil.rmtree(folder_path) # use this to remove tree(nested folders)(directories and content)
#os.remove(my_file_path) # to remove files
"""


# Rename existing folder/file names
root = r"C:\Users\91901\Desktop\stock_feeds"

folder_path = os.path.join(root, r"files_data_new_2")
# source = folder_path
# dest = os.path.join(root, r"myNEWFOLDER")
# os.rename(dest, source)


# Copy files from one path to another path
source = os.path.join(root, 'files_data')
print(source)
dest = os.path.join(folder_path, 'new23333')
print(dest)



# by using shutil module
import shutil

shutil.rmtree(dest)
# copy all files from source to destination
#shutil.copytree(source, dest, dirs_exist_ok=True)


# how do we copy single file
bangalore_file_path = os.path.join(root, 'files_data', 'bangalore.txt')
print(bangalore_file_path)

new_path = os.path.join(folder_path, 'new2', 'MynewFile.txt')
print(new_path)
shutil.copy(bangalore_file_path, new_path)


# copying ways
# 1) all file
# 2) specific files




"""
1) OS(done)(taking time/ learning slowly)
2) SYS(done)
3) shutil(done)
4) csv -->(Done)
5) datetime(Done)
6) json(Done)
7) requests
8) mysqldb
9) sqlalchemy
10) sqlite
11) xlsxwriter
12) timezone in python

Python:

we at least python framword

web : django and flask



Django --> web framework developed in python

url -->
 --> 

front end(UI(html, css, js)(reacJS, vu.js and amgularJS)

backend(Django/flask), java or .net or php)
-> reading or storing




   English --> universal language --> all countries can understand english)
   
   python(dict)  ---?     java    .net     php
   
   
   system A(python)  ----- standard format of data(xml/json/plain text) --> System B(Java)
   ---> python data types(dict) --> json string  --->                   --> Read json --> convert to java data types
        python object <--   json <--                                             <---     json 
          -- dict( java object)
          
          
       finance           admin           wherehouse   
       UI(amazon.com) 
          
"""

















# client server communication with http protocal
# http://dumm.com(browser)   --- DNS  --->   backend server

# app  A                             App B(http://www.fb.com/posts)

# request

# http:
# 1) GET (read)
# 2) POST (writing)
# 3) PUT (update)
# 4) Delete(delete)
# http://www.fb.com/posts
# Get from data from server(GET)

# network
# c ---> s












