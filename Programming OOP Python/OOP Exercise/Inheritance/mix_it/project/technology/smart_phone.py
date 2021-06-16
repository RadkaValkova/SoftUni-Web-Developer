from Inheritance.mix_it.project.technology.technology import Technology


class SmartPhone(Technology):
    def __init__(self, memory, memory_taken):
        Technology.__init__(self, memory, memory_taken)

    def install_apps(self, app, app_memory):
        try:
            memory_left = self.get_capacity(self.memory, self.memory_taken+app_memory)
            self.memory_taken += app_memory
            return memory_left
        except Exception:
            return f'You don\'t have enough space for {app}!'

    # def install_apps(self, app, app_memory):
    #     free_memory = self.memory - self.memory_taken
    #     if app_memory > free_memory:
    #         return f'You don\'t have enough space for {app}!'
    #     self.memory_taken += app_memory
    #     return self.memory - self.memory_taken
