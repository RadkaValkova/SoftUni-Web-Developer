class Hardware:
    def __init__(self, name:str, type:str, capacity:int, memory:int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self,software):
        # if self.capacity < software.capacity_consumption + sum([s.capacity_consumption for s in self.software_components])\
        #         or self.memory < software.memory_consumption + sum([s.memory_consumption for s in self.software_components]):
        #     raise Exception('Software cannot be installed')
        # self.software_components.append(software)
        if self.available_memory < software.memory_consumption or self.available_capacity < software.capacity_consumption:
            raise Exception('Software cannot be installed')
        self.software_components.append(software)

    def uninstall(self,software):
        if software in self.software_components:
            self.software_components.remove(software)

    @property
    def available_memory(self):
        return self.memory - self.used_memory

    @property
    def available_capacity(self):
        return self.capacity - self.used_capacity

    @property
    def used_capacity(self):
        return sum([s.capacity_consumption for s in self.software_components])

    @property
    def used_memory(self):
        return sum([s.memory_consumption for s in self.software_components])

# h = Hardware('a','b',10, 10)
# s = Software('a','b',11, 11)
# h.install(s)