class Equipment:
    id_counter = 1

    def __init__(self, name):
        self.name = name
        self.id = Equipment.id_counter
        Equipment.id_counter += 1

    @staticmethod
    def get_next_id():
        return Equipment.id_counter

    def __repr__(self):
        return f'Equipment <{self.id}> {self.name}'
