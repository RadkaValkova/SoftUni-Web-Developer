class Hero:
    class_name = 'Hero'

    def __init__(self, username, level):
        self.username = username
        self.level = level

    def __repr__(self):
        return f'{self.username} of type {self.class_name} has level {self.level}'


