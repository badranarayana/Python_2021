"""
Data structure
"""

"""
# Basiclly two types data types in python

# 1) Mutable objects(Data can be manipulated from mutable objects)
     operations can perform on mutable objects:  
       # add,
       # removing,
       # updating,
       # read

       #Mutable data types:
       -------------------
       # 1) list
       # 2) dict
       # 3) set

#  2) Immutable objects( data can't be manipulated once object created in memory,
                        can't change/manipulate immutable objects)
     Operation performed on Immutable objects:
     --> only reading, can't manipulate data
     
     # Immutable data types:
      # 1) string
      # 2) tuple
"""

"""
# Data structures in python:
# ------------------------
# 1) List (Mutable object/SEQUENCE)
# 2) string (Immutable object/SEQUENCE)
# 3) tuple (Immutable object/SEQUENCE)
# 4) dict (Mutable object)
# 5) set (Mutable object)
#
#
# primitive data type in python:
# -----------------------------
# 1) int
# 2) float
# 3) complex
# 4) bool(True/False)
#
"""
#
"""
# Date structure:
# --> the way we organize our data to efficiently/easily do read/write/delete.
# """
#
#
"""
# 1) List:
---------
# What is list?
# --> List is mutable object in python
# --> we can create list by using square brackets [ ] or list()
# --> in list we can store any kind of python object(heterogeneous)
# means, list can store number types, string, tuples, dict, set, list
#   example :
#      my_detail = [1, 2, True, "Badra", "Bangalore", 12.4, [2,3,4,4,4,4], 1, 2, 3, (1,2,3,3) ]
# --> We can manipulate the data in list, because it is mutable object
#
#
# Syntax:
---------
# [] # Empty list
# [1, 2, 3] # list with 3 items
# or
# list() # Empty list
# list(1,2,3) # list with 3 items
"""
#
salaries = [1000, 2000, 3000, 1000, 3000, 500, 300]  # new list

# Program #1: Accessing elements from list by using for loop

# iterate/loop over a list object
for salary in salaries:
    print("Salary: ", salary)

# Program #2: access element by using index position
# Index position( starts 0 and end n-1)
"""
# salaries = [100, 200, 300, 400]
#     index    0     1    2    3
#
# Index start from 0 and end n - 1
# q) How items stored in list?
# --> Items stored in list by using index position
"""

# list indexing:
# --------------
"""
Syntax:
------
 sequence[index_value]
"""
# example #1 on indexing
numbers = [1,2,3,3,4,6]
#          0 1 2 3 4 5
first_element = numbers[0]
print(first_element)
third_value = numbers[5]
print(third_value)
print("---------------------------------------------------------------")
#

# Example 2 on list indexing
names = ["Badra", "Srinu", "Raja", "Mani"]
#
# fetch "strinu"
print(names[1])
print("---------------------------------------------------------------")
"""
Note:
----
We can access items from the list with positive index value and negative index value
positive : 0 and n-1( forward access)
negative : -1 and  -n( backward access)
-4   -3  -2   -1
[1, 2, 3, 4]
 0  1  2  3
"""
# Example #3 on indexing
names = ["Badra", "Ashok", "Adhi", "rrr"]

# access elements by +ve index
print(names[1])
# Access elements by -ve index
print(names[-2])
print("-----------------------------------------------------")
# # Index out of range
# print(names[-4])
# # IndexError: list index out of range


"""
slicing:
--> way to get the range of data by providing start index and end index

list Slicing in python:
----------------------
data = []
data[start_index: end_index: step]

"""
# Example #1 on slicing a list:
locations = ['Hyderabad', "Bangalore", "Chnannai", "Mumbai", "Pune"]
print("************* slicing output **************************")
print(locations[1]) # Indexing
my_new_list = locations[2:100] # Returns new list(excludes last value)
print(my_new_list)
print("---------------------------------------------------")

# Example #2 on slicing
numbers = [1, 2, 3, 4, 5, 6, 7]
print(numbers[2:4])
print("----------------------------------------------------")

# Example #3 on slicing with step
# # step :1 default
# # step 2:
print("Step:", numbers[3::2])
print("----------------------------------------------------")

"""
Home work: 
take all asian country names in list, and access each one 
with positive index value and -ve index value
"""

# Adding Data to List:

# How many ways we can add data to the list?
# first approach
data = []
data[0] = 1
print("Data", data)

# Second approach using append method
data2 = [1, 3, 5, 6, 7]
data2.append(10.5)
data2[6] = 10
print("Data2", data2)
print("--------------------------------------------------")

"""
We can do some operations by using builtin function and list methods

Built-in functions:
 1) min
 2) max
 3) all
 4) any
 5) len
 6) dir
 7) help
 8) sorted

List object specific methods:

 1) append
 2) clear
 3) copy
 4) count
 5) extend
 6) index
 7) insert,
 8) pop
 9) remove
 10) reverse
 11) sort
"""

# Applying Built-in function on list
#------------------------------------
# Example #1:
# Write a program to print max number from list of number?
numbers = [-2, 1, 2, 3, 4, 5, 610, 30, 40] # sequence object
print("Max:", max(numbers))
print("Min:", min(numbers))
#

# Example #2
# write a program to find all are values or not
data = [0, 0, 0, None, "Mani"] # 5

# all() Returns true only all items available
print("All return value:", all(data))

# any() returns True if any of the value available
print("Any return value:", any(data)) # or
#
# Example #3
if any(data):  # True/False
    print("We have at least one availbale")

if all(data):
    print("All are valide objects, no empty strings, 0, False, None")

# Example #4: write program to find the length of list
print("list length: ", len(data))
data.append(20)
print("list length: ", len(data))

# Note: we can use len() function find length of sequence object(list, tuple, string)

# len(10) # not supported
# len(True) # not supported
# len(data) # supported
# lets list out all attributes of given object
print(dir(data))
print(dir((91,23)))

print("**************************built in functions done ************************")
print("************************************** lets use list methods ******************************")

#1. list.append()
data = [ ]
data.append(1)
data.append(2)
data.append(0)
print(data) # [1, 2, 0,]
# adding new list using append
for i in [1,2,3,4]:
    data.append(i)
data.append([1,2,3,4])
print("Append data: ", data)
#2. list.extend()
data.extend([1,2,3,4,4,4,4,4,4,4])
print("Extend Data: ", data)

# Write a program to extend one list with another list
names = ["badra", "Srinu"]
another_name = ['raja', 'mani', 'pavan']
names.append("srini1223")
names.extend(another_name)
print(names)
#
#3.insert()  # insert value at specific location(Insert object before index. )
data = ['naga', 'mani', 'naga']
data.insert(1, "pavan")
print(data)

#4. count(object), count the occurrence of given item
# count = data.count(12)
# print(count)
#
# # Removing/delete data from list
# data = [1, 2, 3, 4, 4,4,4]
#
# #data.clear()
# print(data)
#
# # remove/pop
# data.remove(4)  # it remove first occurrence of object()
# print(data)
#
# # pop() default index -1
#
# data.pop()  # remove and return item at the index
#
# print(data)
#
# # pop with index value
#
# data.pop(3)
# print(data)
# removed_item = data.pop(1)
# removed_item1 = data.remove(3)
# print(data, removed_item, removed_item1)
#
#
# # find the list index value with object name
#
# data = ["srinu", "Badra", "Badra"]
#
# index = data.index('Badra')
# print(index)
#
#
# # ordering, sort(), reverse()
#
#
# data = [2,3,1,3,78,8,8,82,3,3,3,1,2,3]
#
# # write a program to sort the list ascending order(asc)
# data.sort()
# print(data)
#
# # Write a program to sort descending order (desc)
# data = [2,3,1,3,78,8,8,82,3,3,3,1,2,3]
# data.sort(reverse=True)
# print(data)
#
# data = [2,3,1,3,78,8,8,82,3,3,3,1,2,3]
# data.reverse()
# print(data)


#------------- list.copy() -------------------
# What is deep copy?

# Deep copy is a process of  making new copy of original object.( and store it into new memory reference)
# physically they have store in different memory references
# cloned copy and original copy not pointed to same reference , they are different.

from copy import deepcopy, copy

colors = ['red', 'green', 'blue']
# using slicing concept
colors1 = colors[:]

# by using copy module deepcopy function
colors2 = deepcopy(colors)

# What is shallow copy?
# Shallow copy is a process of copying reference of original object with out making new copy in memory
# cloned copy and original copy pointed to same object reference

data = [11, 2]

data2 = data  # shallow copy
data3 = copy(data)  # shallow copy
data4 = data.copy()  # shallow copy



data = [1, 2, 3]  # mutable original object

data2 = data  # cloned object/Shallow copy/clone

print(data)
print(data2)

data2.append(20)
data.append(222)

print(data)
print(data2)




# I want to work on new copy without modifying original list



data = [1, 2, 3]

data2 = data  # just copies the object reference. not the value

# how many ways we can do
# 1) by slicing

# Deep copy. it copies values and create new entry in memory
my_copy = data[:]

print(data)
print(my_copy)

# Modify cloned copy
my_copy.append(12)

print(data)  # as is it [1, 2, 3]
print(my_copy) # [1, 2, 3, 12]


data.remove(1)
print("*******************************")
print(data) # [2, 3]
print(my_copy)

new_copy = deepcopy(data)

print(new_copy)

new_copy.remove(3)

print("original", data)
print("Cloned copy", new_copy)



# is, is not

# 'is' returns True if both variables ponted same reference
# shallow copy -- True

# Show do you check clones object is shallow clone or deep clone?
# Ex:
colors = ['red', 'green', 'yellow']
colors_copy = colors[:]
print(id(colors))
print(id(colors_copy))
if id(colors) == id(colors_copy):
    print("Shallow copy")
else:
    print('Deep copy')


if colors is colors_copy:
    print("Shallow copy")
else:
    print('Deep copy')





















































