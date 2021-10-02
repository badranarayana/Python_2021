
# class
# def __



# #def CustomIterator(5):
#
#
# class CustomIterator(object):
#     def __init__(self, num):
#         self.num = num
#         self._num = -1 # 0
#
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self._num == self.num: #0 == 5
#             raise StopIteration("Exhausted")
#         self._num += 1
#         return self._num
#
#
# @logparam
# for i in CustomIterator(10):
#     print(i)
# obj = CustomIterator(5)
# next(obj)
#
#
# from _collections import namedtuple
# namedtuple(field_names=[''])
# l = [12,3,4]
# for i , value numerate(l):
#
# from functools import wraps
#
#
#
# def to_upper(func):
#     @wraps(func)
#     def _upper(*args, **kwars):
#         value = func(args, kwars)
#         if not isinstance(value, str):
#
#
#         return value.upper()
#
#     return _upper
#
# @to_upper
# def hello():
#     """
#     Doc string
#     :return:
#     """
#     return "hello world"
#
#
#
# class Employee(object):
#     _a = None
#     _b = None
#
#     def __init__(self):
#         self.load_data()
#         self.new(10, 20)
#
#     @classmethod
#     def new(cls, a, b, name = "bac" , *args, **kwargs):
#
#         pass
#
#     @staticmethod
#     def load_data(path):
#         return "return file data"
#
#
# Employee.new()
#
#
#
# # GIL(
#
# #thre 1
# #thre 1
# # p
#                        19 (int)
#                       (dhkada7322)
#
# a = 10
# b = a
# import sys
# sys.getrefcount(a)
#
# _, __
#
# def get_data()
#     return self._num

class Demo:
    def __init__(self):
        self._num = 0
        self.__num = 5



obj = Demo()
print(dir(obj))
print(obj._num)
#print(obj.__num)
print(obj._Demo__num)


class myContex(object):

    def __enter__(self,):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


from functools import partial


def multiply(x, y):
    print(f"x=={x}, y=={y}")
    return x * y


doubleNum = partial(multiply, 2)
tripleNum = partial(multiply, 3)

doubleNum(5)


class Signletone:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)

        return cls._instance



obj1 = Signletone()
obj2 = Signletone()
print(id(obj1))
print((id(obj2)))

print("____________________________________")


from stock_feed.read_data import PipeLine

PipeLine(file_path="stock_feed/stock_data.csv").run()
import sys
print(sys.path)



