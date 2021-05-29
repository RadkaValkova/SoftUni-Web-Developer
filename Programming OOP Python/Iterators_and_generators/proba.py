# def hello_func():
#     def sey_hi():
#         return 'Hi'
#     return sey_hi
#
#
# hello = hello_func()
# print(hello())

# def uppercase(fn):
#     def wrapper(*args, **kwargs):
#         result = fn(*args, **kwargs)
#         return result.upper()
#     return wrapper
#
#
# @uppercase
# def say_hi(name):
#     return f'hi {name}'
#
# print(say_hi('Jordan'))
# print(uppercase(say_hi)('Jordan'))
#
#
# def multiply(times):
#
#     def decorator(function):
#         def wrapper(*args, **kwargs):
#             res = function(*args, **kwargs)
#             return res * times
#         return wrapper
#     return decorator
#
#
# @multiply(3)
# def add_ten(number):
#     return number + 10
#
# print(add_ten(3))


class Baba:
    def __init__(self,size):
        self.size = size

    def __repr__(self):
        return f'Baba size is {self.size}'

    def __add__(self, other):
        return Baba(self.size + other.size)


baba_1 = Baba(100)
baba_2 = Baba(10)

print(baba_2+baba_1)




