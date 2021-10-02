
"""
1) Python program to add two numbers
"""

a = 10
b = 20
print(a+b)

# write code to get the user input
#a = int(input("Please enter num1 ")) # str
#b = int(input("Please enter num2")) # str
print(a + b)


# write a program to print first_name
full_name = '. --'#input("Please enter a full name")
if ' ' in full_name:
    first_name = full_name.split(" ")[0] # [str1, str2]
    print(first_name)
else:
    print("Please enter full name with one space")


"""
2) Python Program for factorial of a number?
Factorial of a non-negative integer, 
is multiplication of all integers smaller than or equal to n. 
For example factorial of 6 is 6*5*4*3*2*1 which is 720.

ex:
4! = 4 * 3 * 2 * 1 = 24
"""



num = 6

#n * (n-1) * (n-2) * n-3 ... 1)

fact = 1 # 24

while num >= 1: # 1
    fact = fact * num # 24
    num = num - 1 # 1

print(fact)

"""
Python Program for simple interest

Simple interest formula is given by:
Simple Interest = (P x T x R)/100
Where,
P is the principle amount
T is the time and
R is the rate

EXAMPLE1:
Input : P = 10000
        R = 5
        T = 5
Output :2500
We need to find simple interest on 
Rs. 10,000 at the rate of 5% for 5 
units of time.

EXAMPLE2:
Input : P = 3000
        R = 7
        T = 1
Output :210
"""

P = float(input("Please enter principle amount: "))
R = float(input("Please enter rate of interest: "))  # 2 rupees
T = int(input("Please enter the time in years"))
interest_type = int(input("Enter 1 for simple interest and 2 for compounding interest: "))
if interest_type == 1:
    simple_interest = (P * T * R)/100
    print("Simple interest", simple_interest)

elif interest_type == 2:
    #import pdb;pdb.set_trace()
    principle_amount = P
    times = [1] * T   # [1, 1, 1]
    for t in range(1, T + 1):
        print("TIme: ", t)
        intrest = ((principle_amount) * 1 * R)/100  # p + s_intrest == total
        principle_amount = principle_amount + intrest

    print("Compound interest", principle_amount - P)
else:
    print("Please select valid intrest type")



