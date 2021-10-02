"""

"""
"""
Generator-Function:
------------------
A generator-function is defined like a normal function(def),
but whenever it needs to generate a value, it does so with the yield keyword rather than return. 
If the body of a def contains yield, the function automatically becomes a generator function.


# normal functions returns the values
# generator function returns generator object
"""

def hell():
    print("normal func calling")
    return "Hello"

#print(type(hell))

def hell_gen():
    print("Calling function gen")
    yield "Hello"
    yield "Hello1"
    yield "Hello2"
    yield "Hello3"


#print((type(hell_gen)))

ou1 = hell()
ou2 = hell_gen()
print(ou1) #
print("==>", ou2) #
print("===>", next(ou2))
print(next(ou2))
print(next(ou2))
print(next(ou2))





# tell me out of the program

def print_details():
    print("Prininting Details: ")
    yield "Badra"
    print("Printing salary Details:")
    yield 20000
    print("Printing location details:")
    yield "Hyderabad"

print("**************************************************************")
out = print_details()
print(out)
print("-->", next(out))
print("-->", next(out))
print("-->", next(out))



# write function generate values with gen concept
def my_range(n):
    start = 0
    end = n
    print("Starting while loop")
    while start < end:
        value = start
        start += 1
        yield value
        #yield value
        print("while body")

out = my_range(5)

print(out)
print("***=>", next(out))
print("***=>", next(out))
print("***=>", next(out))
print("***=>", next(out))
print("***=>", next(out))
#print("***=>", next(out))


# when will use generators?
# we use generators when ever you are dealing with large data set and
# entire data set not required at same time.

def file_gen(file_path, max_lines=3):
    start = 0
    with open(file_path, 'r') as file_obj:
        while start < max_lines:
            start += 1
            line = file_obj.readline()
            if not line:
                break
            yield file_obj.readline()


file_path = "files_data/source_data.txt"
out = file_gen(file_path)
print(out)
# print("FILE DATA", next(out))
# print("FILE DATA", next(out))
# print("FILE DATA", next(out))
# print("FILE DATA", next(out))
# print("FILE DATA", next(out))
# print("FILE DATA", next(out))
for line in out:
    print(line)

