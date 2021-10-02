
# Open
# do operations
# close resource(file, db connection or other ports)

# fileobj = open("test_context.txt", 'w')
#
# print("Before writing")
# # do our job
# fileobj.write("Writing data to file")
# raise ValueError("Some wrong data")
#
# print("After writing")
# # close
# fileobj.close()


# Exception handling
try:
    # keep code expecting to raise error
    fileobj = open("test_context.txt", 'w')

    print("Before writing")
    # do our job
    fileobj.write("Writing data to file")
    #raise ValueError("Some wrong data")

except ValueError as error:
    print("ERROR", error.args)
finally:
    # always executes it
    print("inside finally")
    # close
    fileobj.close()


# setup phase for opening resource

# teardown phase closing resource

# context manager is class that class contains two special methods
# __enter__()
# __exit__()


with open("test_context.txt", 'r') as fileobj1:
    # ---
    # --
    # --
    pass



class MyContextManager:
    def __init__(self, fileName):
        self.fileName = fileName

    def __enter__(self):
        print("Opening Resource")
        return "__enetr__ output"
        # retrun the open resource

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exist function")
        print("closing resources")

print("___________________________________")
with MyContextManager("test_context.txt") as obj:
    print(obj)
    #raise ValueError("Somthing wrong")


print("Out side")


class FileManager:
    def __init__(self, filename, mode="r"):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.opened_file = open(self.filename, mode=self.mode)
        return self.opened_file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.opened_file.close()

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

with FileManager('test_context.txt', mode="w") as fileObj2:
    print("Writing to file", fileObj2.name)
    fileObj2.write("Writing from context manager context")

print("OUTSIDE CONTEXT MANAGER")


