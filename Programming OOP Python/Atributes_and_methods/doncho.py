# # variant 1
# def f1():
#     x = int(input())
#     y = int(input())
#     result = x + y
#     print(result)


# Correct Variant
def f2(x, y):
    result = x + y
    return result


def solve():
    x = int(input())
    y = int(input())
    result = f2(x, y)
    print(result)


# input, expected output
tests = [
    ([1, 2], 3),
    ([3, 5], 8),
    ([-3, 3], 0)
]


def execute_tests(func, params, expected_output):
    output = func(*params)
    print(f'Input: {params}, Actual: {output}, Expected: {expected_output}, Correct: {output == expected_output}')

[execute_tests(f2,params, expected) for params,expected in tests]

# from datetime import date
#
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def from_birth_year(cls, name, birth_year):
#         return cls(name, date.today().year - birth_year)
#
#     def display(self):
#         print(self.name + "'s age is: " + str(self.age))
#
#
# person = Person.from_birth_year('John', 1984)
# print(person.__dict__)
# person.display()