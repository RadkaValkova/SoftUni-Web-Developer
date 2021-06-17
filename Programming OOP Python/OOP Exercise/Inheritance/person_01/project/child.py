# from Inheritance.person_01.project.person import Person
from project.person import Person

class Child(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

# person = Person("Peter", 25)
# child = Child("Peter Junior", 5)
# print(person.name, "Peter")
# print(person.age, 25)
# print(child.__class__.__bases__[0].__name__, "Person")