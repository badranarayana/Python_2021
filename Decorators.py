"""
Decorators:
"""
"""
Decorators:
----------
Decorators are very powerful and useful tool in Python 
* since it allows programmers to modify the behavior of function or class. 
* Decorators allow us to wrap another function in order to extend the behavior of 
  the wrapped function, without permanently modifying it.
  
object(function or class) wall

decorator object is to provide additional functionality to exiting object without modifying it.  
"""

def add(a, b):
    print("Adding numbers")

def div(a,b):
    print("Dividing...")

# add some additional

# def add(a, b):
#     print("Adding numbers")
#     print("logging input paraamters")



#add(1, 10)


"""
Syntax:
------
def outerfunc(func):
    def innerfunc(*args, **kwargs):
        # before executing
        out = func(args, kwargs)
        # after executing
        return out
    return innerfunc


def add(a, b):
    return a + b

"""


# lets create decorator that should print parameter of function(it is common requirements)

"""
notes:
# decorator nothing but a python function.

1) decorator takes func as argument/parameter
2) decorator returns inner func object

"""

def log_input_params(func):
    def inner_func(*args, **kwargs):
        print("FROM DECORATOR: ", args, kwargs)  # additional functionality
        out = func(*args, **kwargs)
        return out
    return inner_func


# applying decorator func to callable

@log_input_params
def add(a, b):
    print("Executing add func")
    return a + b

@log_input_params
def div(a, b):
    print("Executing div func")
    return a / b

out = add(10, 20)
print(out)
out2 = div(20, 5)
print(out2)

# out = log_input_params(add)
# out_value = out(10, 20)
# print(out_value)


# write a decorator to check account is active or not
def is_account_active(func):
    def check_account_status(*args, **kwargs):
        account_number = kwargs.get('account_number')
        # write logic to check active or not in db
        is_active = db_query(account_number)
        if is_active:
            print("Account in active status")
            out = func(*args, **kwargs)
            return out
        else:
            print("Account is deactivated. you can't do any transactions.")

    return check_account_status

def db_query(account):
    return False

@is_account_active
def withdraw_money(account_number=None, amount=None):
    print("Withraw success")

out = withdraw_money("1234", 1000)

