class Animal:
    def eat(self):
        return 'eating...'


class Dog(Animal):
    def bark(self):
        return 'barking...'


class Cat(Animal):
    def meow(self):
        return 'meowing...'


a = Animal()
d = Dog()
c = Cat()
print(a.eat())
print(d.eat())
print(d.bark())
print(c.eat())
print(c.meow())