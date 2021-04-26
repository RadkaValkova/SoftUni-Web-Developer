# def get_info(**kwargs):
#     name = kwargs['name']
#     town = kwargs['town']
#     age = kwargs['age']
#     return f'This is {name} from {town} and he is {age} years old'
#
#
# print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))
#
# def get_info(name, town, age):
#     return f'This is {name} from {town} and he is {age} years old'
#
#
# print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))
ll = [1, 2, 3]
print(*ll)
dd = {"name": "George", "town": "Sofia", "age": 20}
print(*dd)
