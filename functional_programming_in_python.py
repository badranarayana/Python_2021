"""
functional programming in python:

Map
filter
reduce
"""

"""
1) map(func, iter): map takes function object and iterable as arguments

"""

# convert all chars to upper case
data = ['badra', 'satys', 'mani']
# o/p : ['BADRA', "SATYS", "MANI"]

out = []
for name in data:
    cap_latter = name.upper()
    out.append(cap_latter)

print(out)

output = map(lambda x: x.upper(), data)
print(list(output))

# we have two iterable objects
first_names = ['badra', 'mani']
last_names = ['Alavaa', "g"]

# ['badra alavala', 'mani g']

out_names = []
for index, first_name in enumerate(first_names):
    full_name = first_name + ' ' + last_names[index]
    out_names.append(full_name)

print(out_names)

#
out = []
for first_name, last_name in zip(first_names, last_names):
    full_name = first_name + ' ' + last_name
    out.append(full_name)

print(out)

# map
out = map(lambda f_name, l_name:  f_name + ' ' + l_name, first_names, last_names)

print(list(out))

# dict
data = {'f_name': "Badra", 'l_name': 'alavala'}

# {'full_name': "Badra alavala"}

full_name = data['f_name'] + data['l_name']


# write a program to sum two list elements

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
list3 = [1, 1, 1, 1]
# out =   [5, 7, 9, 11]

# map

out = map(lambda x, y, z: x + y + z, list1, list2, list3)
print(list(out))


# Map(done)



# filter

# it is used to filter the data and return filtered data


def is_he_tax_payer(name):
    tax_payers_data = {
        'badra': False,
        'mani': True,
        'pavan': False

    }
    return tax_payers_data.get(name)

ap_peoples_list = [{"name": "badra", "annual_income": 30000},
                   {"name": "mani", "annual_income": 40000},
                   {"name": "pavan", "annual_income": 50000},
                   ]


tax_payers_data = filter(lambda person_rec: is_he_tax_payer(person_rec['name']), ap_peoples_list)

print(list(tax_payers_data))
no_tax_payers_data = filter(lambda person_rec: not is_he_tax_payer(person_rec['name']), ap_peoples_list)
print(list(no_tax_payers_data))



# phone boox

contacts = [
    {'name': "badra", 'phone_numbers': "9200202002", 'is_best_friend': True},
    {'name': "badra1", 'phone_numbers': "9200202002", 'is_best_friend': False},
    {'name': "badr2", 'phone_numbers': "9200202003", 'is_best_friend': True},
    {'name': "badr3", 'phone_numbers': "9200202005", 'is_best_friend': False},
    {'name': "badr4", 'phone_numbers': "9200202007", 'is_best_friend': True}

]



# sending marriage invitation to only best friends

def send_invitation(message, contacts):
    # contacts list
   best_friends = list(filter(lambda frd: is_my_best_friend(frd), contacts))
   for contact in best_friends:
       print("Dear ", contact['name'])
       print(message)

def is_my_best_friend(friend_details):
    return friend_details['is_best_friend']

message = """
Please come to my wedding function and bless us
"""


send_invitation(message, contacts)


# Filter with two iterables
data = [10, 3, 4, 8]
data2 = [9, 6, 4, 8]
# [(10, 9), (3, 6), (4,4), (8, 8)]

# out [4, 8] # at index level

print(list(filter(lambda arg: arg[0] == arg[1], zip(data, data2))))

print(list(zip(data, data2)))



# Functional programming

# 1) map
# 2) filter
# 3) reduce

import functools

# reduce
#functools.reduce()

data = [1, 2, 3, 4, 5]
# sum of data (1 + 2 + 3 + 4 + 5)
#  15
value = functools.reduce(lambda x, y: x + y, data)
print(value)

total = 0
for i in data:
    total += i
print(total)


def add_number(x, y):
    result = x + y
    print(f"{x} + {y} = {result}")
    return result

data = [1, 2, 3]
sum_value = functools.reduce(add_number, data, 500)
print(sum_value)



"""
rating:

1) very slow class ?
2) fast class ?


# No questions
--> 
--> 
-->
-->
-->

"""



