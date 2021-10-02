"""
Comprehensions in python

"""
"""
Comprehensions in Python provide us with a short and concise 
way to construct new sequences (such as lists, set, dictionary etc.) 
using sequences which have been already defined. 
Python supports the following 4 types of comprehensions:

1) List Comprehensions
2) Dictionary Comprehensions
3) Set Comprehensions
4) Generator Comprehensions

"""

data = [1,23,4,4,4]
# find even
out = []
for i in data:
    if i %2 ==0:
        out.append(i)

print(out)
# lets implement same thing in List comprehention
even_number = [i for i in data if i % 2 == 0]
              # 3     1 ------------->2
print(even_number)

"""
1) List comprehension:
---------------------
List comprehension provides us elegant way to create new list

syntax:
------
[expression loopings conditions]
[value for value in data] # condition optional
[value for value in data if value % 2 == 0]


# nested loops
[item for item in data for value in item <optional if>]
"""

# write a program to find name starts with "s"
data = ['srinu', 'mani', 'satya', 'raja', 'siva']

# I want a new contains whose name starts with 's'

out_names = [name for name in data if name.startswith("s")]
print(out_names)

# Write a program to convert Upper case
upper_names = [name.upper() for name in data]
print(upper_names)

# tuple
data = ('male', 'female', 'other')
# ["MALE", "FEMALE", "OTHER"]
#out = list(data)
#print(out)
upper_gender = [gender for gender in data]
print(upper_gender)

# Write a program to extract key from dict that key starts with "personal"

bio_data = {
    'personal_name': "Badra",
    "personal_age": 29,
    "personal_loc": "Hyd",
    "professional_company": "Capgemini"
}

# list ['personal_name', 'personal_age', 'personal_loc']

personal_keys = [key for key in bio_data if key.startswith("personal")]

print(personal_keys)

# print persopnal info
for key in personal_keys:
    print(key, "----->", bio_data[key])


# Write a program to find out overs in a given string
vowels = ('a', 'e', 'i', 'o', 'u') # char in vowels
name = "Badaranarayanreddy alavala"
out = [char for char in name if char in vowels]
print(out)

# as of now we seen only single loop
data = [[1,2,3,4],
        [1,4,5,6,7,8,88,88],
        [100,3,4,4]]

def is_even_number(num):
    return True if num % 2 == 0 else False

# find even numbers
for i in data:
    for j in i:
        if is_even_number(j):
            print(j)

# implement nested loops in list comprehension
even_numbers = [num for item1 in data for num in item1 if is_even_number(num)]
print(even_numbers)



# Flatten a list

data = [[1,2,3,4],
        [1,4,5,6,7,8,88,88],
        [100,3,4,4]]

#out_put = [1,2,3,4,1,4,5,6,7,8,88,88,10,100,3,4,4]
# clasical ways
out = []
for item in data:
    out.extend(item)

print(out)
# list
out2 = [value for item in data for value in item]
print(out2)


"""
Dictionary Comprehensions:
--------------------------
Extending the idea of list comprehensions, 
we can also create a dictionary using dictionary comprehensions. 
The basic structure of a dictionary comprehension looks like below.

output_dict = {key:value for (key, value) in iterable if <condition>}

"""
# We have data = [1, 2, 3, 4, 5, 6]
# o/p" {1:1, 2: 2, 3:9...}

data = [1, 2, 3, 4, 5, 6]

out = {value: value**3 for value in data}
print(out)


# simple example
states = ['AP', 'TG']
capitals = ['Vizag', 'Hyderabad']
# How do you create dict and that contains {'state_name': 'cap_nam'}.

#zip()
state_capitals = {state: capital for state, capital in zip(states, capitals)}

print(state_capitals)

def get_capitale(state_name):
    return state_capitals.get(state_name)

# get the TG cap name
print(get_capitale('TG'))

peoples_data = {"badra": 15, "Mani": 17, "Satay": 26}

# filter this dict. create new dict to store filter data
# filter : age > 18
adults = {name: age for name, age in peoples_data.items() if age > 18}
print(adults)
#------------------------------------------------------------------
# Saturday(12-06-2021):

"""
Set comprehensions:
------------------
Set comprehensions are pretty similar to list comprehensions. 
The only difference between them is that set comprehensions use curly brackets { }. 
Let’s look at the following example to understand set comprehensions.

Syntax: 
------
   {expression for item in iterable if conditional}



Example #1 : 
Suppose we want to create an output set which contains 
only the even numbers that are present in the input list. 
Note that set will discard all the duplicate values. 
Let’s see how we can do this using for loops and set comprehension.
"""

# How do you create a set
# {1, 3,4, 4 }, {'key': "va"}

my_data = {1, 2, 3, 3, 4}
print(type(my_data))

#data = {"a":1, "b":2}
#print(type(data))
# set don't allow duplicate values

data = [1,2,3,4,4,545,1,2,3]
# remove duplicates from list
# set
unique_data = set(data)
print(list(unique_data))

# try to  create set with duplicate values
data = {1, 2, 3, 4, 1, 2}
print(data)

# dealing with two sets
set1 = {1, 2, 3, 4, 5}
set2 = {1, 10, 3, 4, 5, 6}

out = set1.union(set2)
print(out)



names = ["badra", "raghu"]
name2 = ["mani", "badra", "satya", "raja"]

# want a new list contains only unique names
# ['badra', 'raghu', 'mani', 'satya', 'raja']

out = []
for name in names:
    if name not in out:
        out.append(name)

for name in name2:
    if name not in out:
        out.append(name)
print(out)

# write above code using sets
names = ["badra", "raghu"]
name2 = ["mani", "badra", "satya", "raja"]
set1 = set(names)
set2 = set(name2)
# create new set from both the sets with unique data
out = set1.union(set2)
print(list(out))

# find the names which are not available in other list
names = ["badra", "raghu"]
name2 = ["mani", "badra", 'raghu', "satya", "raja"]

set1 = set(names) # uni
set2 = set(name2) # uni

out = set1.intersection(set2)
print(out)


# Write a program to find the common items in two list
data1 = [1, 2, 3, 4]
data2 = [5, 3, 1, 10]

out = set(data1).intersection(set(data2))
print(out)

# find out names who are getting the both the pensions from govt?

retired_pension_list = ['badra', 'raghu', 'srinu']
govt_pen_list = ['Satya', 'raja', 'pavan', 'srinu', 'badra',]

# who are getting both pension

retired_set = set(retired_pension_list)
govt_set = set(govt_pen_list)

out = retired_set.intersection(govt_set)
print(out)


data = [1, 2, 3, 4, 5, 6, 7, 8, 910, 1, 2, 3, 4]
# even numbers and remove duplicate values
#set()
out = {i for i in set(data) if i % 2 ==0}
print(type(out)) # it should return the set object

"""
Generator Comprehensions:
------------------------
Generator Comprehensions are very similar to list comprehensions.
One difference between them is that generator comprehensions use circular(parenthesis '( )' ) brackets
whereas list comprehensions use square brackets. 
The major difference between them is that generators don’t allocate memory for the whole list. 
Instead, they generate each value one by one which is why they are memory efficient. 
Let’s look at the following example to understand generator comprehension:

syntax:
------
   (expression for item in iterable if conditional
"""

#out = iter(range(10)) # [1...10]
#print(out)
#print(next(out))
#print(next(out))
#print(next(out))
#print(next(out))

#print(list(out))

#for i in out:
#    print("===>", i)

# out_data = [1, 23, 4]
# print(out_data[0])
# for i in out_data:
#     print(i)


# list comp ==> list
# dict comp ==> dict
# set comp ==> set
# generator expression/comp ==> generator object



# write a program to find even number with large data set
even_generator_object = (i for i in range(100) if i %2 == 0) # gen expression
#print(list(even_generator_object))
# for i in even_generator_object: # next(even_generator_object)
#     print(i)

# print(next(even_generator_object))
# print(next(even_generator_object)) # feacting is completed
# print(next(even_generator_object))  # StopIteration error
# print(next(even_generator_object))
#print(next(even_generator_object))

for i in even_generator_object:
    print("===>", i)



















