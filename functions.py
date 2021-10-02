"""
Python is general purpose
1) scripting,(done)
2) procedural(inprogres)
3) object oriented programming


"""

"""
What is function?
* Function is block of organized code that could be execute when we call function
* function having arguments/paramater to pass input data while calling function
   * required argumnets/parameter
   * positional arguments/arbitary arguments
   * keyward arguments
   * default arguments
* function by default return None if any thing not returning explicitly
* function uses 'return' :keyword to return output
* in python function can return more than one value 



Syntax:
-------
def <function_name>(arguments):
    <state..1>
    <state..2>
    return output

"""

def add(a, b):
    #print(a + b)
    return a + b

result = add(10, 30)

print(result)

def abc():
    return "a","b", "c"
print(abc())
# Write a function to find the value in list or not

def is_found(data, item):
    return item in data

data = (1,2,3,4,4,5,5)

# calling functions
print(is_found(data, 2))

def factorial(number):
    """
    this function is used to find the factorial number of n
    #n * (n-1) * (n-2) * n-3 ... 1)
    :param number: positive int
    :return: int()
    """
    fact = 1
    while number >= 1:
        fact = fact * number
        number = number - 1
    return fact


print(factorial(3))
print(factorial(4))
print(factorial(5))


"""
built-in functions:
------------------
(all, any, max, min, dir, id, type)
these are comes with python software

user defined functions:
----------------------
defined by programmer for project use cases
  --> normal functions(def)
  --> lambda function/anonymous function (lambda)

"""

# 06-05-2021

# Defining normal function
def get_students_list():
    # logic to make a connection to db and fetch the students
    data = [{'name': "Badra"}, {'name':"Satya"}]
    return data

a = 2
print(id(a))
# calling function
print(get_students_list())


# function arguments/paramters:
"""
1) Required/positional arguments
2) arbitrary args
3) Keyword args
4) default args
"""

# define a function with required args
# if function having required args ,
# means we should pass data for those args other wise function will raise error

def mul(a, b):
    return a * b

# calling function
out = mul(10, 5)
print(out)

# usecase2:
# get employee details by id
def get_emp_by_id(id):
    data = {
        1: {'name': "Badra"},
        2: {'name': "Mani"}
    }
    return data.get(id, "Employee not found")


#
b = 10
print(get_emp_by_id(b))
# arbitory args

def add(a,b, *args):
    print("Arbitory args", args)
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(10, 30))


# NOte: args data will be available as tuple object in function

# Complted: requires args and arbitrary args




# 10, 20 ,20, 30, 40, 50



# Define a function that capable of taking more value input data

def myfunc(*args):
    # args = ()
    print(args)


# define function to demonstrate required args
def myfunc_with_re_args(salary, days):
    # function scope
    # two args will will be local varaible in function
    print(salary, days)

#-------------------------------------------------------------------
# 07 - 05 -2021
# Topic: Keyword arguments(**kwargs)
#        default arguments(var = <value>)



# required args(a, b, c), arbitory args(*args)

# define a function that takes keyword arguments

print("*******************************************")
def myfunc_kward(**kwargs):
    print(kwargs)

# Note : keyword args optional

#myfunc_kward()

myfunc_kward(name="Badra", age=30, location="Hyd", state="TG", dob="10/03/1991") # name="Badra", age=20

#myfunc_kward(a=10)

# write a function to store employee details


# take input from user
# store data base

print("********** all args *********************")
def insert_record(name, age, c, d, *args, emp_no="0000", loc="HYD", **kwargs):
    # position/required + arbitrary(*args)  + default arg + kwargs
    # we make connection db
    # store into db
    print("Posinal arg: ", name, age, c, d)
    print("Default args: ", emp_no, loc)
    print("Arbitrary args: ", args)
    print("kwargs", kwargs)
    pass



insert_record("Badra", 2,2, 2)
# **kwargs

# default args





"""
types of function args:
-----------------------
1) positional or required args(values should pass to these args while calling function)
2) Arbitrary args(*args) ( these are optional)
     ex: 1, 2, 4, 5, 4
3) Default Args(key=<Default_value>, ex:- loc="HYD")
     (you can pass new value while calling function, other wise it uses default value) 
4) Keyword args(**kwargs): (these are optional)
    ex: key1=1, key2=2
    
What is the use of retunn statement?
--> return statement is used to return data from the function.

What is the output of function if no return statement?
--> Python function returns None if no return statement in thefunction.


In what order we define all arg types of function?
1) positional args
2) Arbitrary args
3) Default args
4) keyword args



def myfun(a, *args, c=10, **kwargs):
   pass
   

ex:
def add(a, b):
   c = a + b
   print(c)

out = add(10, 20)
print(out) # None


Q) Is it mandatory to pass *args?
ans: arbitrary args are optional

Q) is it mandatory to pass **kwargs?
ans: Optional

Q) is it mandatory to pass default?

ans: default args are optional, 
but if you want to pass new value then you should use default arg name(Mandatory) 

# How do you define a function?
ans: by using 'def' keyword
   def <func_name>(params/args):
       <state..1>
       <state..2>
"""

"""
date: 25-05-2021

Lambda functions in python:
--------------------------

* Lambda function is small anonymous(no name) function
* A Lambda function can take any number of arguments, but can only have one expression.
* by using 'lambda' keyword, we can create function instead of 'def'
* lambda function returns lambda function object 
* lambda function syntax restricted to define in single line

Syntax:
------
 lambda <args>: expression


Use cases:
---------
* frequently use lambda function as inline model for instant usage(no reusable)

* sorting list by specific key

* map, filter

"""



# Define lambda function
add = lambda a, b: a + b
print(add)

print(add(10, 20))

def abc():
    return "values"

print(add(20, 30))
print(abc())





# sort a employee data by employee age asc

employees = [
    {'name': "Badra", 'age': 29},
    {'name': "Mani", 'age': 25},
    {'name': "paavn", 'age': 22}
]
# sort the data by using age
employees.sort(key=lambda dict: dict['name'])

# def key_data(dict):
#     return dict['age']
#
# employees.sort(key=key_data, reverse=True)
print(employees)

# Write a program to convert all string to upper case
colors = ['blue', 'red', 'green', 'yellow']
#colors = ['BLUE', 'RED']
# Map, filter
out = map(lambda x: x.upper(), colors)
print(list(out))


def upper(item):
    return item.upper()

out = map(upper, colors)
print(list(out))

# List of tuples
records = [(6, 1, 3), (1, 3, 4), (2, 4, 5)]

def key_data(row):
    return row[2]

records.sort(key=key_data)
records.sort(key=lambda x: x[2]) # lambda

print(records)


#
def operation(func, a, b):
    return func(a, b) # div(10, 20)


def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def div(a, b):
    return a/b

# DO all operations
a = 10
b = 20

for func in [lambda a, b: a + b, lambda a, b: a - b, div]:
    print(func)
    # what type object you are dealing with
    # number
    # list
    # function
    # funct()
    # object is function means can callable ()
    out = operation(func, a, b)
    print(out)


#
def abc():
    pass

func = lambda : "3"

print(abc())

print(func())



def get_chars(item):
    if item.isalpha():
        return item

def get_numaric(item):
    if item.isnumeric():
        return item

def apply_filter(filter_func, data):
    out = []
    for item in data:
        ot = filter_func(item)
        if ot:
            out.append(ot)
    return out

data = ['abc', '1233', "zyx123"]

chars = apply_filter(get_chars, data)
print(chars)
nums = apply_filter(get_numaric, data)
print(nums)

nums = apply_filter(lambda x: x if x.isnumeric() else '', data)
print(nums)



def mvAverage(stock_name):
    print(f"applying moving average on {stock_name}")
    return True

def EMACroseOver(stock_name):
    print(f"Applying EMA corss over on stocks {stock_name}")
    return True


def place_order(qty, stock_name):
    print("Placing order")
    return True


def apply_stratgy(strategy, stock_name):
    buy_signal = strategy(stock_name)
    if buy_signal:
       order = place_order(qty=100,
                    stock_name=stock_name)
       # stop loss
       # target

    else:
        # sett order
        pass


is_placed = apply_stratgy(mvAverage, 'Apl')
if is_placed:
    print("Order placed")

is_placed = apply_stratgy(EMACroseOver, 'SBI')
if is_placed:
    print("Order placed")


for i in ['aple', 'sbi', 'tcs']:
    for stretegy in [mvAverage, EMACroseOver]:
        is_placed = apply_stratgy(stretegy, i)
        if not is_placed:
            is_placed = apply_stratgy(EMACroseOver, i)
            # transactions
            # buy:
            # sell
            # stop_loss



# Process 1--> mv:

# process 2 --> em

# process 3 -->


#2 sec --> stragies --> found oder_plce (skip)
#2 sec --> EMA --> places (skip)


# What are the difference normal/function and lambda/anonymous function?

"""
  Normal function                         Lambda function
 ------------------                      -----------------
 1) we use 'def' keyword to define       1) We use 'lambda' :keyword to define it
    normal function
 2) Normal function can have any number  2) It can have only single line statement
    of statements in body                    due to syntax restriction.
 3) we can provide function name while   3) it is anonymous function, we can't give func name
    defining it.
 4) it returns values by using 'return'  4) no return keyword used here.
    :keyword
 5) it return the values                 5) it returns function object.
 
 Examples:
 # sum of two number                     # sum of two numbers
 def add(a, b):                           lambda a, b: a + b
     return a + b

 6) It can be reusable any               6) We use lambda functions as inline model and instance
  where with function name                  purpose
   add(10, 20)                              ex: sorting complex object . sorted(), map(), filter()

"""

# take use case and implement it by using functions

# Employee
# organization details
# presonal
# address
# payroll details
# Department details

def print_organization_details():
    print("Capgemini")
    print("Bangalore")

def print_persanal_details():
    print("Name: Badra")
    print("Age: 29")
    print("Date of Birth: 10-04-1991")

def print_employee_address():
    print("Address: Hyderabd")


def pay_roll():
    print("Salary: 40000")

def department():
    print("Cloud dept")

def get_employee_details(details_type):
    if details_type == 'full':
        # org specific
        print("Org details:")
        print_organization_details()
        department()
        pay_roll()

        # personal details
        print("Personal details:")
        print_persanal_details()
        print_employee_address()
    elif details_type == 'personal':
        print_persanal_details()
        print_employee_address()

    elif details_type == "org":
        print_organization_details()
        department()
        pay_roll()

    elif details_type == 'payroll':
        pay_roll()

    elif details_type == 'dept':
        department()

    elif details_type == 'empaddr':
        print_employee_address()



# client

print("****************************************************************")
get_employee_details(details_type='personal')






# use case: Bank transaction

# check balance
# mini statement
# deposit
# withdraw
# opening account
# disable account
# close account
# passbook details

bank_balance = 3000

def open_account(adhar, pan, photo):
    # adhar and pan
    if not adhar:
        print("adhar card is required to open account")
    if not pan:
        print("pan card is required to open account")
    if not photo:
        print("Photo is required to open account")
    if adhar and pan and photo:
        print("Opening bank account....")
        print("Account created successfully..")


def close_account(account_number, proof):
    if not account_number:
        print("Account number is required to close it")

    if not proof:
        print("Proof required to close it as per govt guide lines")
    if account_number and proof:
        print("closing account Done!.")


def disable_account(account_number, reason="No tractions since 1 year"):
    pass

# tractions deposit and withdraw

def deposit_amount(account_number, amount):
    pass


def withdraw_amount(account_number, amount):
    # min_bal
    global bank_balance
    if check_balance(account_number) - amount < min_balance():
        print("No balance..")
    else:
        bank_balance = bank_balance - amount
        print("Withdraw done.")


def min_balance():
    return 2000


def check_balance(account_number):
    return bank_balance


def build_mini_statement(account_number):
    pass

def passbook_details(account_number):
    pass


data = [1,2,3,4,5]
data2 = [2,3,5,9,6]

out = filter(lambda item: item in data2, data)
print(list(out))

data = [3, 4, 5, 10, 24, 44, 22, 29]
even = filter(lambda x: x % 2 == 0, data)

print(list(even))


def myfilter(func, iterable):
    out = []
    for item in iterable:
        op = func(item)
        if op:
            out.append(item)

    return out


print(help(list))

"".center()

output = myfilter(lambda item: item % 2 == 0, data)
print(output)

# uppers listout
data = ["ABC", "anc", "XYZ"]

out = myfilter(lambda item: item.isupper(), data)
print(out)


# functions (Done)











































