from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, 'Power', int(capacity*0.25), int(memory*1.75))
        # super().__init__(name, type='Power', capacity=capacity, memory=memory)
        # self.capacity = int(capacity * 0.25)
        # self.memory = int(memory * 1.75)

# ph = PowerHardware('a', 10, 10)
# print(ph.__dict__)