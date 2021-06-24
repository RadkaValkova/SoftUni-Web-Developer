from project.software.software import Software


class LightSoftware(Software):
    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name=name, type='Light', capacity_consumption=capacity_consumption, memory_consumption=memory_consumption)
        # super().__init__(name, 'Light', int(capacity_consumption*1.5), int(memory_consumption*0.5) може и така
        self.capacity_consumption = int(capacity_consumption * 1.5)
        self.memory_consumption = int(memory_consumption * 0.5)


# l = Software('s', 'c', 50, 10)
# ll = LightSoftware('s', 'c', 50, 10)
# print(l.__dict__)
# print(ll.__dict__)