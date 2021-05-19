class Equipment:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.name}'


a = Equipment('aaa')
b = Equipment('bbb')
print(a.name)

getattr()
