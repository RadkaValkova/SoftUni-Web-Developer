from Inheritance.mix_it.project.technology.technology import Technology


class Laptop(Technology):
    def __init__(self, memory, memory_taken):
        Technology.__init__(self, memory, memory_taken)

    def install_software(self, software, software_memory):
        try:
            memory_left = self.get_capacity(self.memory, self.memory_taken+software_memory)
            self.memory_taken += software_memory
            return memory_left
        except Exception:
            return f'You don\'t have enough space for {software}!'


    # def install_software(self, software, software_memory):
    #     free_memory = self.memory - self.memory_taken
    #     if software_memory > free_memory:
    #         return f'You don\'t have enough space for {software}!'
    #     self.memory_taken += software_memory
    #     return self.memory - self.memory_taken
