"""
Modules and Packages in python
"""

"""
modules and packages:

 -> python modules and packages, two mechanisms 
    that facilitates modular programming


what is modular programming?
 
 -> Modular programming refers to the process of breaking
    a large programming task into separate, smaller,
    more manageable subtasks or modules.
    
 -> Individual modules can be clubbed togethar like
    building blocks to create a larger application
 
 Advantages to modularizing 
 code in large application:
 --------------------------
   1) Simplicity:
       ----------
      -> Rather than focusing on entire problem at hand,
      
        A module typically focuses on relativly small portion of
        a problem. This makes development easier and less error-prone.
        
   2) Maintainability:
   
      -> Modular are designed in that way to have logical boundaries. 

   3) Reusability:
   
      --> Functionality defined in a single module can be 
      easily reused (through an appropriately defined interface) 
      by other parts of the application. 
      This eliminates the need to duplicate code.
      
   4) Scoping:
     --> Modules typically define a seperate namespace,
     which helps avoid collisions between identifiers
     in different areas of program.
     
     xyz.py
     ------
     a = 10
     b = 20
     
     abc.py 
     -----
     a = 30
     b = 20
     
     
     final.py
     -------
     #from xyz import a
     #from abc import a
     import xyz
     import abc
     # avoid collision b/w identifiers
     print(xyz.a)
     print(abc.a)
     
     
     

Note: Functions, modules and packages 
      are all constructs in Python that promote 
      code modularization.
      


How to define a modules in python?

--> There are actually three different ways 
    to define a module in Python 
   
   1) A module can be written in python itself
   
   2) A module can be write in 'C' language and 
      Loaded dynamically at run time , like re module
      
   3) A built-in module is intrinsically 
      contained in the interpreter, like the itertools module.
      
  --> python  --> some of the code already available in other language -->
  
  
         stocks  -> c language

--> python  --> cython intherface --> c libs
"""


"""
How to create a module in python

how to create packages in python

how to create package to distribute to other project or pip install?


What is module?
--> module is python file having collections of identifiers(Variables, functions, classes)..

what is python package?
--> python package is python directory contains one special __init__.py
--> package contains collection of modules as well as sub packages
    india
      __init__.py
      abc.py --> module
      xyz.py --> module
      AP
        __init__.py
        ap_module1.py --> get_schemes() --> list()
        ap_module2.py
        guntur
            __init__.py
      
      TG
        __init__.py
        tg_module1.py --> tg_schemes() --> list()
        tg_module2.py


main.py
------
get_scheme:
# I want to find out AP schemes

# importing entire module
#from india.AP import ap_module1

# importing specific identifier from modules
from india.AP.ap_module1 import get_schemes

out = get_schemes()

# I want to find out TG Schemes

# imorting entire module
# from india.TG import tg_module1

from india.TG.tg_module1 import tg_schemes
out2 = tg_schemes()

"""



"""
HR Management:
-------------

--> Department
     --> dept.py

--> Employee
     --> emp.py

--> payroll
     --> payroll.py
     


main.py
------

def get_dept_details():



"""









































