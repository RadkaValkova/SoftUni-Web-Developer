# from wild_cat_zoo_01.project.caretaker import Caretaker
# from wild_cat_zoo_01.project.cheetah import Cheetah
# from wild_cat_zoo_01.project.keeper import Keeper
# from wild_cat_zoo_01.project.lion import Lion
# from wild_cat_zoo_01.project.tiger import Tiger
# from wild_cat_zoo_01.project.vet import Vet


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.__budget = budget
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__animal_capacity > 0 and self.__budget < price:
            return 'Not enough budget'
        elif self.__animal_capacity <= 0:
            return 'Not enough space for animal'
        self.__budget -= price
        self.__animal_capacity -= 1
        self.animals.append(animal)
        return f'{animal.name} the {animal.class_name} added to the zoo'

    def hire_worker(self, worker):
        if self.__workers_capacity <= 0:
            return 'Not enough space for worker'
        self.workers.append(worker)
        self.__workers_capacity -= 1
        return f'{worker.name} the {worker.class_name} hired successfully'

    def fire_worker(self, worker_name):
        if self.workers:
            worker = [w for w in self.workers if w.name == worker_name][0]
            if worker in self.workers:
                self.workers.remove(worker)
                self.__workers_capacity += 1
                return f'{worker_name} fired successfully'
        return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        sum_workers_salary = sum([worker.salary for worker in self.workers])
        if sum_workers_salary <= self.__budget:
            self.__budget -= sum_workers_salary
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'
        return f'You have no budget to pay your workers. They are unhappy'

    def tend_animals(self):
        sum_animals_needs = sum([animal.get_needs() for animal in self.animals])
        if sum_animals_needs <= self.__budget:
            self.__budget -= sum_animals_needs
            return f'You tended all the animals. They are happy. Budget left: {self.__budget}'
        return 'You have no budget to tend the animals. They are unhappy.'

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        animals = {'Lions': [el for el in self.animals if el.class_name == 'Lion'],
                   'Tigers': [el for el in self.animals if el.class_name == 'Tiger'],
                   'Cheetahs': [el for el in self.animals if el.class_name == 'Cheetah']
                   }
        result = f'You have {len(self.animals)} animals\n'
        for key, value in animals.items():
            result += f'----- {len(animals[key])} {key}:\n'
            for el in value:
                result += f'{el}\n'
        return result.strip()

    def workers_status(self):
        workers = {'Keepers': [el for el in self.workers if el.class_name == 'Keeper'],
                   'Caretakers': [el for el in self.workers if el.class_name == 'Caretaker'],
                   'Vets': [el for el in self.workers if el.class_name == 'Vet']
                   }
        result = f'You have {len(self.workers)} workers\n'
        for key, value in workers.items():
            result += f'----- {len(workers[key])} {key}:\n'
            for el in value:
                result += f'{el}\n'
        return result.strip()


# zoo = Zoo("Zootopia", 3000, 5, 8)
#
# # Animals creation
# animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4),
#            Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]
#
# # Animal prices
# prices = [200, 190, 204, 156, 211, 140]
#
# # Workers creation
# workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68),
#            Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280),
#            Vet("Sam", 29, 220)]
#
# # Adding all animals
# for i in range(len(animals)):
#     animal = animals[i]
#     price = prices[i]
#     print(zoo.add_animal(animal, price))
#
# # Adding all workers
# for worker in workers:
#     print(zoo.hire_worker(worker))
#
# # Tending animals
# print(zoo.tend_animals())
#
# # Paying keepers
# print(zoo.pay_workers())
#
# # Fireing worker
# print(zoo.fire_worker("Adam"))
#
# # Printing statuses
# print(zoo.animals_status())
# print(zoo.workers_status())

#     # def test_zoo_hire_worker_success(self):
# z = Zoo("Some Zoo", 1500, 1, 1)
# print(z.hire_worker(Vet("I am Vet", 20, 500)))
# print(len(z.workers), 1)
# print(z._Zoo__workers_capacity, 1)