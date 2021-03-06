from statistics import mean


class CalculateAverageMixin:
    def get_average(self, values):
        return mean(values)


class MathUtils:
    def get_average(self, values):
        return mean(values)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person, CalculateAverageMixin):
    def __init__(self, name, age, grades):
        super().__init__(name, age)
        self.grades = grades

    # това е по правилният вариант от миксин
    def get_average_grade(self):
        return MathUtils().get_average(self.grades)


class Employee(Person, CalculateAverageMixin):
    def __init__(self, name, age, daily_working_hours):
        super().__init__(name, age)
        self.daily_working_hours = daily_working_hours


st = Student('Pesho', 18, [2, 3, 5, 6, 6, 6])
print(st.get_average(st.grades))
print(st.get_average_grade())
