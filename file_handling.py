"""

"""

"""
File modes:
----------

r:
Opens a file for reading only. The file pointer is placed at the beginning of the file. This is the default mode.

rb
Opens a file for reading only in binary format. The file pointer is placed at the beginning of the file. This is the default mode.

r+
Opens a file for both reading and writing. The file pointer will be at the beginning of the file.

rb+
Opens a file for both reading and writing in binary format. The file pointer will be at the beginning of the file.

w
Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.

wb
Opens a file for writing only in binary format. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.

w+
Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.

wb+
Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.

a
Opens a file for appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.

ab
Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.

a+
Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.

ab+
Opens a file for both appending and reading in binary format. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.

"""


# How to open a file and read the data in python?
# ans: By open() function, we can deal with file operations(opening file)


# How to use open()
# opening file
file_object = open("phonebook.txt") # 'r'

# read content
#file_data = file_object.read() # it reads entire file content as string
file_data = file_object.readline()
file_data1 = file_object.readline()
file_data2 = file_object.readline()
file_data3 = file_object.readline()
print(type(file_data))
print("file content:", file_data)
print(file_data1)
print(file_data2)
print(file_data3)
# close file
file_object.close()


print("*** readline in loop")
# readline in side loop

file_object = open("phonebook.txt") # 'r'

print(type(file_object))

for line in file_object:
    print(line)

file_object.close()


# verify the output of read, readline, readlines
print("*** Verify output of file object methods ****")
# open #1
file_obj = open("phonebook.txt", 'r')

# Lets call our file obj methods #2
# it reads entire file content and retrun as string
print(file_obj.read())
# it returns empty string here. because file pointed touches the last already
print("read 2", file_obj.read())
# if trying to read data that already read by program?
# get empty string. because pointer there last line.
# how to read it again?
# have to reopen the file to read it one more time
#file_obj2 = open("phonebook.txt", 'r')
#print("file 2: ", file_obj2.read())
# closing #3
file_obj.close()


# Test the readline()
print("Readline output **********************")
f_obj = open('phonebook.txt', 'r')

# readline() read line by line as string
line_1 = f_obj.readline()
line_2 = f_obj.readline()
line_3 = f_obj.readline()
print(line_1)
print(line_2)
f_obj.close()

# advatages:
# * Memory efficient due to have single line in memory at a time
# use case: read only first 10 lines
file_obj = open('phonebook.txt', 'r')
print("___________________________________________")
read_rows = 1
for i in range(0, read_rows):
    line = file_obj.readline() # read()
    print(line)

file_obj.close()

#--------------------------------------------------------

# 02 - 06 - 2021:
# how to open a file and read data?

# how many ways we read data?
# 1) read() reads the entire file object and returns string
# 2) readline() reads one line at time and return string
# 3) readlines() reads the entire file  and return list of lines
     # ex: [line1, line2, line3.....]

# readlines()

# open file
file_obj = open('phonebook.txt', 'r')


def get_dict_from_file(file_name):
    file_obj = open(file_name, 'r')
    header = file_obj.readline()
    column_names = header.split(",")
    column_names = [col.replace('"', '') for col in column_names]
    # read the content of file
    lines = file_obj.readlines()
    #print(lines)  # all lines of data stored into program memory
    data = []
    for line in lines:
        out = { }
        colums_data = line.split(",") # ['', '']
        for index, col_data in enumerate(colums_data):
            column_name = column_names[index].replace("\n", '')
            out[column_name] = col_data.replace("\n", '')
            if '"' in out[column_name]:
                out[column_name] = out[column_name].replace('"', '')
        data.append(out)
    # close
    file_obj.close()

    return data


phone_records_dict = get_dict_from_file('phonebook.txt')
print(phone_records_dict)

locations = get_dict_from_file('abc.txt')
print(locations)

indexes_dict = get_dict_from_file('stock_indexes.csv')

import pprint
pprint.pprint(indexes_dict)

# --------------------------- 06-0-2021(sunday) ----------------------------------
# Writing file
# writing content from one file to another with some filter criteria
# single file - read operation
# single file write -- write operations/creating new file/modifying file

# How do we write the data in to file?

# Open a file in order read/write data in file

print("******************* write file opertion **************************")
file_name = "user_details1.txt"
# file modes
# 'r' - read mode
# 'w' - write
# 'a' - append mode
# 'r+' - read write
# 'w+' -> write and read
# 'a+' --> append and read
# 'rb' - read binary mode
# 'wb' - write binary mode

file_obj = open(file_name, 'a')


employee_data = "Badra,\t10-02-1992,\thyderabad1234444\n"

#Note:
# Python will create a file if dosen't exist in harddisk in case file open with 'w' mode
# if open with 'r' mode, python will raise filenotfound error
file_obj.write(employee_data)

file_obj.close()

# What is the difference b/w 'w' and 'a' mode?
# -> file opened with 'w' mode will removes the old
#    content while add new content(previous data overridden by new data)
#  -> file opened with 'a' mode will append the content after last line in exiting file.
#     means in this process we won't loss previous written data in file.


# when will you use 'r' mode?
# when your intention is to just do read operation on file then we use 'r' mode
#ex:
file_read_object = open('user_details.txt', 'a+') # default is 'r' mode

print(file_read_object.readable())
print(file_read_object.writable())
file_read_object.seek(0) # pointes to the chanrs
print("File:", file_read_object.read())
file_read_object.write("I am new to python\n")
file_read_object.seek(0) # it sets the offset 1
print("File:", file_read_object.readlines())
file_read_object.close()

# -------------------------------------------------------

# Handling two files for reading and writing
# input file
# out put file
# requires 2 files , 1. input file 2. output

# copying data from one file to another file

def filter_data(line, location=None):
    columns_data = line.split(",")
    loc = columns_data[1]
    if loc == location:
        return True
    else:
        return False


def copy_data(src_file, dst_file, location='hyd'):
    # opening file with context managers, python will close opened file automatically
    with open(src_file, 'r') as src_file_obj:
        with open(dst_file.format(location=location), 'a') as dst_file_object:
            headers = src_file_obj.readline()
            # reading from source file
            for line in src_file_obj:
                is_filter_passed = filter_data(line, location=location)
                if is_filter_passed:
                    # writing to dest file
                    dst_file_object.write(line)

    print("COPYING DONE....")


src_file_name = 'files_data/source_data.txt'
dst_file_name = 'files_data/{location}.txt'
copy_data(src_file_name, dst_file_name, location="pune")

# File concept completed.



# comprehenstions
# 1) list comprehestion
# 2) tuple..

# generators & iterators
# decorators

# object oriented programming(class)
# built -in modules
# packages and module.
# third party modules and pip


# only in python


# Django framework --> needs lot of effert(only passion)


































