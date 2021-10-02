


# LOOPS
# 1) for loop
# 2) while




"""
for loop:
Syntax:
for <variable_name> in <sequence/iterable object>:
    str1
    st2
    st3

str4


"""


names = ['Badra', 'Mani', "Raja", "Naga", "Pavan"]

# Write a program to convert each name into upper case and print

for name in names: # 'badra', 'Mani', 'Raja', 'Naga', 'pavan'
    # convert to upper
    uper_name = name.upper()
    print(uper_name)

print("out side loop")


# Write a program to print 1 to 4 numbers
# range(0,11)
# numbers = list(range(1, 12))
# print(numbers)

# for num in range(1, 5):
#     print(num)


# Write a progam to add 2 to the each number in list
#data = [1,2,3,4,4,4]
for i in range(1, 100):
    out = i + 2
    #print(out)




# Where we can use for loop
# ans: we can use for loop on sequence/iterable objects
# sequences: string, list, tuple
# iterable: string, list, dict

# Write a program to print all char in string
location = "Banaglore"
for char in location:
    #print(char)
    pass

# Write a program to get the asci values of each char in string
name = ""
for char in name:
    # write a logic to find the asci value
    asci_value = ord(char)
    print(asci_value)

# loop over tuple
locations = ("hyd", "bng", 'cni')

for loc in locations:
    print(loc)
print("****************************************************")
# Write a program to find even and ord number between 1 to 20
data = range(1, 100)
# even or odd number logic
for i in data:
    # Write even number logic
    if i % 2 == 0:
        print("Even : ", i)
    else:
        print("Odd :", i)

print("*****************************************************")




# Table


table_num = int(input("Please enter table num: "))
# 10
numbers = range(1, 11)
for num in numbers:
    out = table_num * num
    print(table_num, " * ",  num, " = ", out)






















