
# write a program to print 1 to 10 with out using for loop/built-in methods

start = 1
end = 100

while start <= end: #5 <= 10(True)
    print(start)
    start += 1 # 5

# Write a program to print even number between 2 to 10
# 2, 4, 6,8, 10

start = 0
end = 10

while start <= end: # 11 <= 10 (False)
    if start == 0:
        print(1)
    print(start)
    start += 3



# What is the difference between for loop amd while?

#1) While loop iterates as long as condition in True
#) For loop iterates over the sequence until last item

# in while we should take care about loop termination
# for loop we no need to do any termination, because for loop knows the length of sequence

#
count = 0
while count <= 5:
    print("Infinite")
    count += 1

print("Out side")

#
for i in range(10):
    print(i)



# How do you define a while loop in python?
# -> we use while key word followed by condition and :
# --> we define body/block of while loop
# We should make sure increment/decrement to terminate loop



# How do you define for loop in python?
# --> we use for keyward followed by variable and 'in' sequence
# --> for loop iterations depends on length of sequence




# How do you break the loop in python?


target = 5

for i in range(10): # [0,1,2,3,4,5,6,7,8,9]
    if i == target:
        print("Target found")
        break  # terminate the loop
    print("Searching for target")


print("*******")
for i in range(12): #11
    if i == 11:
        print("We found target")
        break #
    print("Hell")

print("out side loop")

# What is the use of break and where will you use it?
# We use 'break' statement only inside loops(for/while)
# break statement terminates loop and control goes out the loop body/block




# Write a program to break while loop when num is 5


num = 0


while num <= 7:
    if num == 2:
        print("Breaking  loop......")
        break
    print(num)
    num += 1





# continue: used to skip the current iteration

# Write a program to print 1 to 10 nums except 3, 7, 6?

for i in range(0, 11): # 4
    if i not in [3, 7, 6]:
        continue  # skip the current iterations

    print(i)

print("***********************************************")
num = 0

while num <= 5:
    if num in [1, 4]:
        num += 1
        continue
    print(num)
    num += 1


