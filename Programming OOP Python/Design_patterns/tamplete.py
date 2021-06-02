from abc import ABC, abstractmethod


class Employee:
    def __init__(self, first_name, last_name, job_title):
        self.first_name = first_name
        self.last_name = last_name
        self.job_title = job_title

    def __repr__(self):
        return f'{self.first_name} {self.last_name}: {self.job_title}'


class EmployeesList(ABC):
    def __init__(self):
        self.employees = []

    @abstractmethod
    def order_by(self, x):
        pass

    def add_employee(self, employee:Employee):
        self.employees.append(employee)

    def list_employees(self):
        ordered_employees = sorted(self.employees, key=lambda x: self.order_by(x))
        return ordered_employees


class EmployeesListByFirstName(EmployeesList):
    def order_by(self, x:Employee):
        return x.first_name


class EmployeesListByLastName(EmployeesList):
    def order_by(self, x:Employee):
        return x.last_name


el = EmployeesListByFirstName()
el.add_employee(Employee('pesho', 'ivanov', 'manager'))
print(el.list_employees())
