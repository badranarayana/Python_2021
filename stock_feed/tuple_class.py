

"""
What is tuple?

* Tuple is immutable sequence object in python
* immutable means we can't manipulate the data once tuple object in created
* tuple is almost equal to list object, except  mutable behaviour
* We can access elements/Items from tuple by using index position(tuple sequence object)

Operations:
* Read

Syntax:

my_type = (1,2, 3,4 4)

my_type1 = (1, )

or
my_typle = tuple()


# Built-in methods
sum, max, min, len, dir, help, sorted, reverse

# tuple methods
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |
 |  index(self, value, start=0, stop=2147483647, /)
 |      Return first index of value.
 |
 |      Raises ValueError if the value is not present.
 |

# Looping

"""


# Defining a tuple

gender = ("Male", "Female", "Other")

print(gender)

# Accessing elements from tuple object
# Indexing

male = gender[0]
print(male)

# Access last it from tuple

other = gender[-1]
print(other)

# fetch the female value
female = gender[1]
print(female)


# applying bult-in functions

# sum, max, min, len, dir, help, sorted, reverse

salaries = (5000, 100, 300, 500)
print("Sum of salaries: ", sum(salaries))
print("max salary", max(salaries))
print("min salary", min(salaries))
print("num of salaries:", len(salaries))
print("Sorted tuple: ", sorted(salaries))
print("Reverse", tuple(reversed(salaries)))
print(salaries)

print("****************** Help *************************")
print(help((1,)))


colors = ("green", 'red', 'yellow', 'yash', 'yellow1') # Tuple object
index = colors.index('yellow')
print(index)
count = colors.count("yellow")
print(count)

"""
What is difference between list and tuple?


list                          tuple
----                          -----
1) it is Mutable object       1) It is immutable object(can't manipulate data)
2) list brakets[] to define   2)  tuple uses () to define tuple
3) access using index         3) access using index
4) it is sequence object      4) it is also a sequence object

ex:                            ex:
colors = ['red', 'blue']          colors = ('red', 'blue')




How do we convert tuple into list?

Type casting --> convert one datatype to other compartable data type

my_colors = ('red', 'blue')

# Converting tuple into list object
my_color_list = list(my_colors) # list object , mutable
my_color_list.append("Yellow")

How do we convert list into tuple?
my_colors = ['red', 'green', 'yellow']

# typecast list into tuple
my_tuple = tuple(my_colors) # Tuple




How do we convert '1' into int?

emp_num = "1001"
emp_num = int(emp_num)
print(type(emp_num))


# Convert int to a string?
str(1) # '1'


# What is the out put of following program?

data = "112333123"
int(data)


"""
# How do we iterate over a sequence object in  python?
# 1) for loop
# 2) while loop
print("*****************for loop***********************")
data = [1, 2, 3, 4]
for i in data:
    print(i)


# while works based condition
print("*************************** While loop ***************************************")
length = len(data) # 4
count = 0
while count < length: #False
    # indexing
    value = data[count]  # data[3]
    print(value)
    count += 1


















