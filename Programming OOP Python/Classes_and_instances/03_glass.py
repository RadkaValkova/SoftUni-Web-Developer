class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0

    def fill(self, ml):
        if Glass.capacity >= ml:
            self.content += ml
            Glass.capacity -= ml
            return f'Glass filled with {ml} ml'
        return f'Cannot add {ml} ml'

    def empty(self):
        Glass.capacity = 250
        self.content = 0
        return 'Glass is now empty'

    def info(self):
        return f'{Glass.capacity} ml left'


glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())
