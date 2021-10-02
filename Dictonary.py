"""
Dictionary:
---------
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable(mutable) and does not allow duplicates.
Dictionaries are written with curly {} brackets, and have keys and values:

Syntax:
------
my_dict = { }  # empty dictionary

my_dict = {'name': "badra", 'age': 29}  # dict with items

# Creating dict from iterable object

my_dict = dict(iterable) # creates a new dict object from iterable object


Dict methods:
|  clear(...)
 |      D.clear() -> None.  Remove all items from D.
 |
 |  copy(...)
 |      D.copy() -> a shallow copy of D
 |
 |  get(self, key, default=None, /)
 |      Return the value for key if key is in the dictionary, else default.
 |
 |  items(...)
 |      D.items() -> a set-like object providing a view on D's items
 |
 |  keys(...)
 |      D.keys() -> a set-like object providing a view on D's keys
 |
 |  pop(...)
 |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
 |      If key is not found, d is returned if given, otherwise KeyError is raised
 |
 |  popitem(self, /)
 |      Remove and return a (key, value) pair as a 2-tuple.
 |
 |      Pairs are returned in LIFO (last-in, first-out) order.
 |      Raises KeyError if the dict is empty.
 |
 |  setdefault(self, key, default=None, /)
 |      Insert key with a value of default if key is not in the dictionary.
 |
 |      Return the value for key if key is in the dictionary, else default.
 |
 |  update(...)
 |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
 |      If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
 |      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
 |      In either case, this is followed by: for k in F:  D[k] = F[k]
 |
 |  values(...)
 |      D.values() -> an object providing a view on D's values
 |
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |
 |  fromkeys(iterable, value=None, /) from builtins.type
 |      Create a new dictionary with keys from iterable and values set to value.
 |
"""


# Example #1 Create dictionary to store employee details like name, age, salary, location, employee number etc.


# creating dictionary
employee = {
    'employee_number': 1,
    'name': "Pavan",
    'age': 22,
    'salary': 50000,
    'location': "Hyderabad"
}
# access data from the dict

# we access data using key
# incase of sequence object(list, tuple, string) we use index position

# get the employee number
print(employee['employee_number'])
print(employee['age'])

# location of employee
print(employee['location'])

# name of the employee
print(employee['name'])


# What will happen when we access data with key that doesn't exist in dict?
#print(employee['mobile_number'])

# How to add a data to dictionary

person_details = {'name': "Srinu", "dob": "10/02/1991", 'location': "Bidhar"}
# adding new pair/item

person_details['mobile_number'] = "+91 9010326385"
person_details['address'] = "Hyderand, kphb, 500072"
print(person_details)

print(person_details['mobile_number'])
print(person_details['address'])

person_details['address'] = "Bagalore. 6333377"

print(person_details['address'])
# duplicate keys not allowed
# if we try to add key that alredy exited in dict,
# it will override the value that key with new values

person_details['mobile_number'] = "+1 2556522155"

print(person_details['mobile_number'])


# How do we find the lenght of dict

print(len(person_details))

# How do we create a dict from iterable object
#{"key1": "value1", "key2": "value2"}


my_data = [
    ("key1", "value1"),
    ("key2", "value2"),
    ("key2", "xyz")
] # list of tuples
data = dict(my_data)
print(data)


my_employee_details = [
    ("name", "Badra"), # 0
    ("age", 20), # 1
    ("location", "hyderabad"), # 2
    ("Mobile_number", "+91  9030002020")  # 3
]

# print the phone number?
phone_details = my_employee_details[1]
print(phone_details[1])

# try dict(iterable)

my_details = dict(my_employee_details)
print(my_details['age'])


# Dict specific methods
data = {'name': "Badra"}
print(help(data))
print(data.get('name1', "Key not found"))

print("************************ dict methods ***************************")
# using dict methods
# crete /update delete and read

person = {
    'name': "Mani",
    'dob': "10/03/1993"
}
# how to read the data from thr above dict
# by using key
print(person['name'])

# returns the value of key if key presnt in dict other wise return default value(None)
print("get", person.get("name", "key not found"))

# d1.update(d2)
address = {
    'pin_code': "500072",
    'land_mark': "Near to main road",
    'mandal': "Kphb",
    'location': "Hyderabad"
}
family_details = {
    'father_name': "raju",
    'mother_name': "rani",
    'brother_names': {"y_brother": "raju", 'e_brother': "srinu"},
}
# updating exiting dict with new dict
person.update(address)
person.update(family_details)
print(person)
my_brothers_list = person.get('brother_names')
print(my_brothers_list)
print(my_brothers_list['y_brother'])
print(my_brothers_list['e_brother'])

print(person.get('brother_names')['y_brother']) # {'e_brother': 'venky', 'y_brother':'tarun'}[0]
print(person.get('brother_names')['e_brother'])


# pop, popitem, clear to remove data from dict
person.pop('brother_names') # dict.pop("key")
print("pop out:", person.pop('pin_code') )  # returns the value remove key
print(person)
# lets see what pop is retruning back
# popitem
print("popitem out:", person.popitem()) # retruns tuple object after removing last key:value pair from dict
print(person)


# clear
person.clear() # clear all items from dict
print(person)
person['name'] = "Pavan"
print(person)

# del keywork
print(person)
#del person # delated from memory location
print(person)
# I want to delete a key value with del statement
del person['name']
print(person)
del person
#print(person)
#print(abc)

# keys(), values(), items()
data = {'color': "red", 'width': "20px"}
       # key   : value,  key:  value

print(data.keys())
print(data.values())
print(data.items())

# looping
for key in data.keys():
    print(key, "-->", data[key])

# iterate over values of dict
for value in data.values():
    print(value)

# iterate over dict key and value
for key, value in data.items(): # [('color', 'red'), ('width', '20px')]
    print(key, "--->", value)


# tuple unpacking
data = ('color', 'red')
key, value = data
print(key, value)

# tuple packing
data = 1,2,3,4 # tuple packing
print(data)
num1, num2, num3, num4 = data
print(num1, num2, num3, num4)


data = {
    'voter_name': 'Satya',
    'location': "Vizag",
    'age': 29,
    'parties': ['ycp']
}

# copy(), setdefault, fromkeys()
# setdefault
"""
setdefault(key, default=None, /) method of builtins.dict instance
    Insert key with a value of default if key is not in the dictionary.
    
    Return the value for key if key is in the dictionary, else default.
"""

#print(help(data.setdefault))

print(data.setdefault('age', None))
print(data)


# complex example
print(data.setdefault("parties", []))

# if 'parties' in data:
#     data['parties'].append("ABC")
# else:
#     data['parties'] = ["ABCD"]


print(data)
data['parties'].append("YSRCP")
data['parties'].append("TDP")
print(data)



# insert the key with default value when given key not present in dict
# it won't insert if key present in dict that means it return existing value


print(help(data.fromkeys))

data = ['name', 'location', "state"] # {'name': '', 'location': '', "state": ''}

data2 = {}
new_dict = data2.fromkeys(data, '')
print(data2)
print(new_dict)

if not new_dict.get('name'):
    new_dict['name'] = "New data"

print(new_dict)

# fromkeys logic
def from_keys(iterable, value=None):
    new_dict = {}
    for key in iterable:
        new_dict[key] = value

    return new_dict

print(from_keys(['a', 'b', 'c'], value=''))

# copy()
# shallow copy() and deepcopy()

# shallow copy Copies the reference of object
# deepcopy creates a new copy

data = [1, 2, 3, 4] # mutable object
data2 = data  # copies the reference data
data2.append("my new data")

data3 = data2
data3.append("XYX")
print(data3)
print(data)
print(data2) # shallow copy

colors = ('red', 'blue', 'yellow')
my_colors = colors

# immutable object
# if my_colors is colors:
#     print("Both variables pointed to same object in memory")
# else:
#     print("Both are different objects in memory")

#del my_colors
print(colors)
# reference count(1)


#  how do we do deepcopy()
original_list = [1,2]
new_list = original_list[:] # deep copy

if original_list is new_list:
    print("Same object")
else:
    print("separate objects")

new_list.append("new")
print(original_list)
print(new_list)

# using list comprehension
my_list = []
for i in original_list:
    my_list.append(i)
print("for loop", my_list)
 # or
my_list = [i for i in original_list]
print("compre", my_list)


# built in module
from copy import deepcopy, copy


data = [1,2,3]
new_data = deepcopy(data)
new_data.append("New data")
print(new_data)
print(data)
if new_data is data:
    print("Both are pointed")


# another way
# datastructure method(list, dict)
data = [1,2,3]
data2 = data.copy()

data2.append("New")
print(data)
print(data2)

# Programing on copy and deepcopy
data = [[1, 2], [1, 3]] # [[1, 2], [1, 3]]
data2 = deepcopy(data)
if data[0] is data2[0]:
    print("Same object")
else:
    print("Separate object")


data2[0].append("New item")

print(data)
print(data2)


"""
A shallow copy constructs a new compound object and then (to the extent possible) 
inserts references into it to the objects found in the original.

A deep copy constructs a new compound object and then, 
recursively, inserts copies into it of the objects found in the original.
"""


data = {'a': 20,
        'salaries': {"salary1": 1000}, # mutable
        'colors': ('red', 'gree'), # immutable,
        'phone_numbers': ['phon1', 'phon2']
        }
data2 = data.copy() #deepcopy(data)
data2['a'] = 30
data2['salaries']['salary1'] = "2000"
data2['colors'] = ("red",)
data2['phone_numbers'].append("new phone number")
print(data)
print(data2)

# copy()

def mycopy(iterable):
    new_object = None
    if isinstance(iterable, list):
        new_object = []
    for i in iterable:
        if isinstance(i, int):
            new_object.append(i)
        elif isinstance(i, list):
            new_object.append(i) # copying reference

    return new_object



data = [1,2,3, [1,2,3]]

new_data = mycopy(data) # shallow copy
print(new_data)
new_data[3].append("new item")
print(new_data)
print(data)


# mydeepcopy
def mydeepcopy(iterable):
    iterable_object = None
    if isinstance(iterable, list):
        iterable_object = []

    for i in iterable:
        # if nested mutable object we should make new copy
        if isinstance(i, (int, tuple, str)):
            iterable_object.append(i)
        elif isinstance(i, list):
            new_data = [] # making new copy and string values from object
            for j in i: # []
                new_data.append(j)
            iterable_object.append(new_data)

    return iterable_object

# test
data = [1,2,3, [4,5]]
# make deepcopy
my_copy = mydeepcopy(data)

print(my_copy)
print(data)
my_copy[3].append("New data for deep copy test")
print(my_copy)
print(data)


