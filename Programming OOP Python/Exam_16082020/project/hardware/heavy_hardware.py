from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, 'Heavy', capacity*2, int(memory*0.75))
        # super().__init__(name, type='Heavy', capacity=capacity, memory=memory)
        # self.capacity = int(capacity * 2)
        # self.memory = int(memory * 0.75)