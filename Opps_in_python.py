"""

Object oriented programming in python

Terminologies in opps:
---------------------
1) class
2) object/INSTANCE
3) constructor
4) variables
5) Class variable
6) instance variable
7) Static methods
8) class methods
9) Instance methods
10) Properties
11) Inheritance
12) Magic methods(__method)

4 pillar of oops:

1) Encapsulation
2) abstraction
3) Polymorphism
4) Inheritance


https://www.analyticsvidhya.com/blog/2020/09/object-oriented-programming/

"""

# scripting
# functions (reusabulity) (small unit of reusable code)
# creating structure
# reusabulity

def add(dhhdh):
    pass



# class is blue print to build real object

'''
class <className>:
    # variables
    # methods/functions
'''

# employee operations
class Employee:

    def __init__(self, emp_name, age, location, salary):
        print("INIT")
        self.emp_name = emp_name
        self.age = age
        self.location = location
        self.salary = salary

    def get_emp_details(self):
        print("methon invoking")
        print(self.emp_name)
        print(self.age)
        print(self.location)
        print(self.salary)

    def salary_details(self):
        print("method invoking 2")
        print(self.salary)

    def emp_name(self):
        pass


# create an object/instance of the class
my_obj = Employee(emp_name="Satya", age=25,location="Hyd",salary=2000) # list(), tuple()
# print(my_obj)
my_obj.get_emp_details()
# my_obj.emp_name()
my_obj.salary_details()
#

# Defining class
class Car:
    # constructor
    def __init__(self, name, color, brand):
        self.name = name
        self.color = color
        self.brand = brand

    def get_car_info(self):
        name = self.name
        color = self.color
        brand = self.brand
        print(name, color, brand)

    def get_color(self):
        print(self.color)

    def get_brand(self):
        print(self.brand)

# create object/instance of class
my_car = Car("Desire", "Green", "Maruthi Suziki")
print("********************************************")
# print(my_car.name)
# print(my_car.color)
# print(my_car.brand)


# calling function in object
my_car.get_car_info()
my_car.get_color()
my_car.get_brand()

# lets create another car object
my_car2 = Car("Amaze", 'radiant red', "Honda")
my_car2.get_brand()
my_car2.get_color()



# How do we define a class in python?
# by using class keyword followed by class name
class MyClass:
    # variables
    # functions
    pass

# How do you provide data while creating object of class?
# By using class consstructor that is __init__(self)

class MyClass1:
    # constructor, will be implicitly invoked, while create object of the class
    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age

    def get_age(self):
        return self.age

# How do you create a object/instance of class?
my_obj = MyClass1("Badra", 28)

# how do we initialize the instance variable in class?
# ans: Through constructor of class while creating instance

# How do we define instance method in class?
# Define  method and pass self as first argument.
class ABC:
    def info(self):
        # instance method
        pass

# How do we call instance methods?
# first create the instance of the class
abc_obj = ABC()
# call the instance methods by using class instance and . notation
out = abc_obj.info()


# Lets take one more use case to create a class
# Person
# name,
# eye_color,
# height,
# weight

# actions:
# Speak
# walk
# drink


class Person:
    def __init__(self, name, eye_color, height, weight, play_games=None, singing=None):
        self.name = name
        self.eye_color = eye_color
        self.height = height
        self.weight = weight
        self._play_games = play_games
        self.sining = singing

    def play_games(self):
        if self._play_games:
            print(f"{self.name} Can Play Games")
        else:
            print(f"{self.name} can't play games")

    def can_sing(self):
        if self.sining:
            print(f"{self.name} can sing a songs")
        else:
            print(f"{self.name} can't sing a songs")



# instance 1
mani = Person(name="Mani", eye_color='black', height="5 feets", weight=50, singing=True)
mani.play_games()
mani.can_sing()

# instance 2
pavan = Person(name="Pavan", eye_color='brown', height="6 feets", weight=40, play_games=True, singing=True)
pavan.play_games()
pavan.can_sing()
# -------------------------------------------------------------------------------------
# Instance variables and instance methods(Done)


# Class variables and class methods
# Class is collection data variables and methods
# variables
# 1) instance variables
# 2) Class variables
# methods
# 1) Instance method
# 2) class method
# 3) static method
"""
Class variables and class methods:

"""
# Static data that is common to every object of the class
class School:
    # class variables
    board = "SSC Board"
    board_address = "KPHB, Hyd"

    def __init__(self, name, address):
        # instance variables
        self.name = name
        self.address = address

    def get_school_name(self):
        return self.name

    def get_school_address(self):
        return self.address

    @classmethod
    def update_board_address(cls, new_addr):
        cls.board_address = new_addr



zph = School("ZPH", "Hyderabad")
zph.name = "HSHDSSS"
nri = School("NRI", "Guntur")
narayan = School("NARAYANA", "Vizag")

# good practice
School.update_board_address("BAngalore")
# Trying to access instance method with class name
# School.get_school_name() can't access instance methods without instance creation.


# Change the board address
# we have to deal with class methods, because class methods are used to manipulate class variables

#print(zph.board)
print(zph.board_address)
print(zph.get_school_name())
#print(nri.board)
#print(nri.get_school_name())
print(nri.board_address)
#print(narayan.get_school_name())
print(narayan.board_address)

"""
Notes:
1) Class method can be callable with class name, no need to create instance of the class
2) Class method can be callable with instance of that class, 
   but instance methods can't be call by using class 
   
# Instance methods can only call after instance creation.
ex: obj = MyClss()
    obj.instancemethod()
    obj.myClassMethod() # Valid
    
    MyClass.myClassMethod() # valid
    MyClass.instancemethod() # Invalid
    
"""









"""
Date: 03-07-2021(Saturday)

Defining Properties in class:
-----------------------------
The @property decorator is a built-in decorator in Python for the property() function. 
Use @property decorator on any method in the class to use the method as a property.

You can use the following three decorators to define a property:

@property: Declares the method as a property.
@<property-name>.setter: Specifies the setter method for a property that sets the value to a property.
@<property-name>.deleter: Specifies the delete method as a property that deletes a property.


Get data
setting data
deleting data

"""

class Student:
    def __init__(self, name, age):
        self.__name = name # Private variables, only access in side class
        self.age = age

    @property
    def name(self):  # getter property
        print("Invoking getter name property")
        return self.__name

    @name.setter
    def name(self, name): # setting value
        print("Invoking Setter property")
        self.__name = name

    @name.deleter
    def name(self):
        print("Delete property invoking")
        del self.__name

print("*******************************************************************")

obj = Student("Badra", age=20)
print(obj.name)
print(obj.age)
obj.name = "My New name"  # we have to define setter property
obj.age = 30
print(obj.name)

# Delete the property
del obj.name
print(obj)

# name attribute is removed from the self object. so we get attribute error
#print(obj.name)

a = 10
print(a)
del a


"""
Static methods in Class:
------------------------

The @staticmethod is a built-in decorator that defines a static method in the class in Python. 
A static method doesn't receive any reference argument whether it is called by an instance of a class or by the class itself.

@staticmethod Characteristics:
-----------------------------
--> Declares a static method in the class.
--> It cannot have cls or self parameter.
--> The static method cannot access the class attributes or the instance attributes.
--> The static method can be called using ClassName.MethodName() and also using object.MethodName().
--> It can return an object of the class.

"""

def ABC():
    print("FROm ABC")


class StudenClass:
    school_name = "ZPH School" # Class attributes/variables

    def __init__(self, name, date_of_birth):
        self.name = name  # Instance attributes/variables
        self.__dob = date_of_birth

    @staticmethod
    def get_details():
        # This method can't access class attributes and instance attributes,
        # but can be callable with class as well as instance
        print("Getting details from static methods")

    @classmethod
    def get_school_name(cls):
        #print(cls.name) # can't accecss instance attributes in class method
        return cls.school_name

    def get_name(self):
        return self.name

    @property
    def dob(self):
        return self.__dob

    @dob.setter
    def dob(self, dob):
        self.__dob = dob

# Calling static method with classname
StudenClass.get_details()
print(StudenClass.get_school_name())

# calling static method with object/instance
obj = StudenClass(name="Badra", date_of_birth="10/03/1992")
obj.get_details()
print(obj.get_school_name())
print(obj.get_name())
print(obj.dob)


# What are the differences between class method and static method?
"""
   class method                                       static method
   ------------                                       -------------
   1) Declare method as class method with help        1) Declare method as static method with help of @staticmethod decorator
      of @classmethod decorator. 
   2) It can access class attributes,                 2) It can't access either class attributes or instance attributes
     but not instance atrributes
   3) it can call by using class name                 3) same 
       myclass.method()
       with object
        obj.method()
   4) class method take first argument as cls         4) no reference args like cls, self
   
   5) It can be used to create factory method that    5) can't create object as no access to class
      allows to create object of class and return
   

"""


class Car:
    def __init__(self, name, brand, groud_clearence=None):
        self.name = name
        self.brand = brand
        self.ground_clearence = groud_clearence

    @classmethod
    def car_factory(cls, name, brand, vehicle_type):
        if vehicle_type == "SUV":
            obj = cls(name, brand, groud_clearence="2 feets")
        else:
            obj = cls(name, brand, groud_clearence="1.5 feets")
        return obj




# obj = Car(name="Desire", brand="MAruthi")
# obj.

my_obj = Car.car_factory(name="Amaze", brand="Honda", vehicle_type="")
print(my_obj.ground_clearence)

#----------------------------------------------------------------------------


"""
Python Inheritance:
-------------------
* Inheritance allows us to define a class that inherits all the methods and properties 
  from another class.

  Parent class is the class being inherited from, also called base class.

  Child class is the class that inherits from another class, also called derived class.
"""
# Base class


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_person_details(self):
        print(self.first_name, "-->", self.last_name)

# object
obj = Person("mani", "G")
obj.get_person_details()

# create class student
# derived class
class Student(Person):
    # first_name, last_name, graduation_year, roll_number
    def __init__(self, first_name, last_name, graduation_year, roll_number):
        # initialize the base class
        Person.__init__(self, first_name, last_name)
        # child specific variables
        self.graduation_year = graduation_year
        self.roll_number = roll_number

    def get_student_details(self):
        print(self.roll_number, "-->", self.graduation_year)

    def full_details(self):
        data = {
            'first_name': self.first_name,  # coming from parent class
            'last_name': self.last_name,  # coming from parent class
            'graduation_year': self.graduation_year,  # same class
            'roll_number': self.roll_number,   # same class
            "out_put": self.get_person_details()  # calling parent class method
        }
        return data

student1 = Student('Badra1', "Alavala1", 2019, "ABCSD123")
# this method calling from base class
student1.get_person_details()

# this method calling from derived class student
student1.get_student_details()
student_full_detail = student1.full_details()
print(student_full_detail)


# student2 = Student("Mani", "G")
# student2.get_person_details()
"""
Types of Inheritance in python
------------------------------
1) Single level inheritance
2) Multi level inheritance
3) Multiple Inheritance


Advantages of inheritance:
-------------------------
* Inheritance enables reusability of code
* Inheritance can save a lot of time and coding efforts
* Inheritance improves the structure of the program that makes it more readable
* Inheritance makes the code short and concise making it more reliable
* It makes the code easy to debug
"""


"""
1) Single level inheritance:
----------------------------
In python single inheritance, a derived class is derived only from a single parent class 
and allows the class to derive behaviour and properties from a single base class. 
This enables code reusability of a parent class, 
and adding new features to a class makes code more readable, elegant and less redundant


A derived class can extent only single parent class


class Base:
  pass
  

class Derived(Base):
   pass
"""

class A:
    def method1(self):
        print("Method 1 calling from class A")


class B(A):
    def method2(self):
        print("method2 calling from class B")

    def method1(self):
        super().method1() # reusing parent functionality
        # adding additional functionality
        print("Method 1 is calling from class B")


obj_b = B()
obj_b.method2()
obj_b.method1()


"""
2) Multi-level inheritance:
--------------------------
Multi-level inheritance is when a new class is derived, 
by inheriting a class that is derived from some other class.
The program illustrating the implementation of multi-level inheritance is given below.

Base #1  ----> Derived #1(Base #1)  ----> Derived #2(Derived #1)
"""

class Base:
    def base_method(self):
        print("printing from base class")

class Derived_A(Base):
    def method_a(self):
        print("Printing from Derived_A class")

class Derived_Ba(Derived_A):
    def method_b(self):
        print("printing from Derived_B class")


# instance
new_obj = Derived_Ba()
new_obj.method_a()
new_obj.method_b()
new_obj.base_method()

"""
3) Multiple inheritance:
-----------------------
A derived class is inheriting  more than one base class at a time

"""
class ABC:
    def method_abc(self):
        print("ABC from abc")

class XYZ:
    def method_xyz(self):
        print("XYZ")

    def method_abc(self):
        print("ABC from xyz")

class DerivedClass(XYZ, ABC):
    def method_derived(self):
        print("Derived")
# MRO
obj_1 = DerivedClass()
obj_1.method_abc()


# -----------------------------------------------------------------------------
"""
The 4 Principles Of Object-Oriented Programming
1) Encapsulation
2) Abstraction
3) Polymorphism, 
4) Inheritance.

The four pillars for OOP are Abstraction, Encapsulation, Inheritance, Polymorphism.

1) Encapsulation :
-----------------
 Encapsulation means wrapping up data and member function (Method) together into a single unit 
 i.e. class. Encapsulation automatically achieve the concept of data hiding providing security 
  to data by making the variable as private and expose the property to access
  the private data which would be public.

2) Abstraction :
--------------- 
Abstraction is the process of showing only essential/necessary features of an entity/object 
 to the outside world and hide the other irrelevant information. 
 For example to open your TV we only have a power button,
 It is not required to understand how infra-red waves are getting generated in
 TV remote control.

3) Inheritance :
   ------------ 
   The ability of creating a new class from an existing class.
   Inheritance is when an object acquires the property of another object. 
   Inheritance allows a class (subclass) to acquire the properties and behavior of another class (super-class). It helps to reuse, customize and enhance the existing code. So it helps to write a code accurately and reduce the development time.

4) Polymorphism:
  ------------- 
Polymorphism is derived from 2 Greek words: poly and morphs. 
The word "poly" means many and "morphs" means forms. 
 So polymorphism means "many forms".
 
 A subclass can define its own unique behavior and still share 
 the same functionalities or behavior of its parent/base class. 
 
 A subclass can have their own behavior and share some of its behavior 
 from its parent class not the other way around. 
 A parent class cannot have the behavior of its subclass.


1) overloading(no support in python, compiled languages supports it)
2) overriding
"""

class BaseCalculate:
    def add(self, a, b):
        return a + b


class Mycalulator(BaseCalculate):
    # Overriding parent class method
    def add(self, a, b, c):
        res = super().add(a,b) # parent class functionality
        return res + c # child specific functionality

cal = Mycalulator()
cal.add(10, 20 , 30)
# requirements to add 3 number


# Built in function len()
# get length of list
#len([12333,3,3,3,3])
#len("string")



# Use case: Mobile
"""
Attributes:
# Hardware
--> Operating System
--> Processor
--> Battery_Type
--> RAM SIZe
--> ROM
--> extendable memory card (up to some GB)
--> camera_fixels

# Body panel
--> Screen_type
--> body_height
--> body_width
--> finger_print
--> color

# Actions
--> switch on 
--> switch off
--> open_cam
--> take_pic
--> take_video
--> update_settings
--> play_youtube videos
--> connect_wifi
--> search phonebook
--> make call
--> end call
--> answering incomming call

"""


class MobileOS:
    def __init__(self, name, version):
        self.__name = name
        self.__version = version

    @property
    def os_details(self):
        return {"OS_NAME": self.__name,
                "Version": self.__version}


class MobileHardWare:
    def __init__(self, processor, ram, rom, external_memory, battery_type):
        self.__processor = processor
        self.__ram = ram
        self.__rom = rom
        self.__external_memory = external_memory
        self.__batter_type = battery_type

    @property
    def hardware_details(self):
        return {
            "PROCESSOR": self.__processor,
            "RAM": self.__ram,
            'ROM': self.__rom,
            "EXT_MEMORY": self.__external_memory,
            "BATTERY_TYPE": self.__batter_type
        }

    @property
    def get_external_memory_card_capacity(self):
        return self.__external_memory


class MobileBody:
    def __init__(self, screen_type, body_height, body_width, finger_print, color):
        self.__screen_type = screen_type
        self.__body_height = body_height
        self.__body_width = body_width
        self.__finger_print = finger_print
        self.__color = color

    def mobile_body_details(self):
        return {
            "Screen": self.__screen_type,
            "BodyHeight": self.__body_height,
            "BodyWidth": self.__body_width
        }



# Derived Class(Multiple inheritance)
class Phone(MobileHardWare, MobileOS, MobileBody):
    def __init__(self, processor, ram, rom, external_memory, battery_type,
                       name='', version='',
                       screen_type='', body_height='', body_width='', finger_print='', color=''):
        super().__init__(processor,
                         ram,
                         rom,
                         external_memory,
                         battery_type)
        MobileOS.__init__(self, name, version)
        MobileBody.__init__(self,
                            screen_type,
                            body_height,
                            body_width,
                            finger_print, color)

        self.open_cam = False

    def switch_on(self):
        print("switch on the phone.....")

    def switch_off(self):
        print("Switch off the phone....")

    def open_camera(self):
        print("Opening camera..")
        self.open_cam = True
        return self

    def take_pic(self):
        if self.open_cam:
            print("Taking pic")
        else:
            print("first open cam")

    def take_video(self):
        if self.open_cam:
            print("Taking video")
        else:
            print("first open cam")





phoneobj = Phone(processor="Intel",
                 ram="8 GB",
                 rom="60 GB",
                 external_memory="120 GB",
                 battery_type="Litheum",
                 name="Android",
                 version="1.23.4", screen_type="Normal type", body_height="15cm",
                 body_width="8cm",
                 finger_print=False,
                 color="Blue"
                 )

print(phoneobj.hardware_details)
print(phoneobj.os_details)
print(phoneobj.mobile_body_details())
phoneobj.open_camera().take_pic()
phoneobj.open_camera().take_video()

# Apple phone

apple_phone = ""

# onePlus

class CreatePhone(Phone):
    def __init__(self, brand_name, processor, ram, rom, external_memory, battery_type,
                       name='', version='',
                       screen_type='', body_height='', body_width='', finger_print='', color=''):
        super().__init__(processor=processor,
                 ram=ram,
                 rom=rom,
                 external_memory=external_memory,
                 battery_type=battery_type,
                 name=name,
                 version=version,
                 screen_type=screen_type,
                 body_height=body_height,
                 body_width=body_width,
                 finger_print=finger_print,
                 color=color
                 )

        self.brand_name = brand_name

    @property
    def get_brand_name(self):
        return self.brand_name



# Apple phone
apple_phone = CreatePhone(brand_name="Apple",
                       processor="Intel",
                          ram="8 GB",
                 rom="60 GB",
                 external_memory="120 GB",
                 battery_type="Litheum",
                 name="IOS",
                 version="1.23.4", screen_type="Normal type", body_height="15cm",
                 body_width="8cm",
                 finger_print=False,
                 color="Blue"
                 )

print(apple_phone.hardware_details)
print(apple_phone.os_details)
print(apple_phone.mobile_body_details())


# MI phone
mi_phone = CreatePhone(brand_name="MI",
                       processor="Intel",
                          ram="8 GB",
                 rom="60 GB",
                 external_memory="120 GB",
                 battery_type="Litheum",
                 name="IOS",
                 version="1.23.4", screen_type="Normal type", body_height="15cm",
                 body_width="8cm",
                 finger_print=False,
                 color="Blue"
                 )

print(mi_phone.get_brand_name)
print(mi_phone.hardware_details)
print(mi_phone.os_details)
print(mi_phone.mobile_body_details())
mi_phone.open_camera().take_video()

apple_phone.open_camera().take_video()






















































































































