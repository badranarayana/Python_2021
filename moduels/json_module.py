import json
"""
Json module in python:
---------------------
The full-form of JSON is JavaScript Object Notation

JSON OBJECT	  PYTHON OBJECT     JAVA
-----------   ------------      -----   
object	       dict              map object
array	       list              array object 
string	       str
null	       None
number(int)	   int
number(real)   float
true	       True
false	       False

              date or datetime


--> use to transfer data between applications
--> client --> server(who provid service(input/output) json or xml

# use case like
govt data base --> voter service(JSon / Json)

python app ---> filter_data='{'state':'TG', 'area': 'kphb'}' --> voter service(java)
                      '{'voter':[{'name': 'Mani', 'address': "XYX"}, {}, {}]  }'                                       <-- Json resp


# How do we handle json string data in python?

1) converting python objects to json

2) parsing json string to python native objects


# json -- builtin in module in python
"""

print(dir(json))


# dump
# dumps
# load
# loads

my_employees_data = [
    {
        'name': "Srinu",
        'age': 31,
        'emp_id': 1,
        'salary': 50000.50,
        'is_manager': True
    },
    {
        'name': "Mani",
        'age': 25,
        'emp_id': 2,
        'salary': 40000.50,
        'is_manager': False
    }
]
print(type(my_employees_data))
# convert it into json
my_json = json.dumps(my_employees_data)
print(my_json)
print(type(my_json))
# making call to other service


def making_service_call(url, data):
    """
    Simulator like other service
    :param url:
    :param data:
    :return:
    """
    print("Making call to service")
    resp = {
        'status_code': 201,
        'message': "success"
    }
    return json.dumps(resp) # json string

resp = making_service_call(url="http://myorg.com/create_employees", data=my_employees_data)

print(type(resp))
# convert resp json to python object
data = json.loads(resp)
print(type(data))
if data['status_code'] == 201:
    print("RESP", data)

# handling date and datetime with json
from datetime import datetime
from datetime import date

my_details = {
    'name': "Mani",
    'age': 25,
    'dob': date(year=1994, month=5, day=12) # string
}

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        # elif isinstance(obj, datetime.timedelta):
        #     return (datetime.datetime.min + obj).time().isoformat()

        return super(DateTimeEncoder, self).default(obj)

def custom_dump(py_object):
    return DateTimeEncoder().encode(my_details)


obj = custom_dump(my_details)
print(obj)
# lets convert this object into json
#my_json = json.dumps(my_details, default=DateTimeEncoder)
#print(my_json)
# how do we define customer json encoders


data = '{"name": "Mani", "age": 25, "dob": "1994-05-12"}'

# decode json into python object

my_details = {
    'name': "Mani",
    'age': 25,
    'dob': date(year=1994, month=5, day=12) # string
}


json_str = custom_dump(my_details)
print(json_str)
print(json.loads(json_str))

class CustomerJsonDecoder(json.JSONDecoder):
    pass






"""

Json is object/format used to exchange data between two parties(app(python) --> app(java))
app A (python)                                 App B (Java)
 database                                        database

     json  or xml data format used to transfer via network




browser(UI)
"""

# python object --> json string  ------> n/w ..... other app(json string ---> java objects --> program
#laptop pack   ---> ----->     ---> unpack  --> laptop
# python native objects --> json -------------> json ---> python native object

