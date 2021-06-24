class DecorationRepository:
    def __init__(self):
        self.decorations = []   # will contain all decorations (objects).

    def add(self, decoration):
        self.decorations.append(decoration)

    def remove(self, decoration):
        if decoration in self.decorations:
            self.decorations.remove(decoration)
            return True
        else:
            return False

    def find_by_type(self, decoration_type: str):
        elements = [el for el in self.decorations if el.__class__.__name == decoration_type]
        if elements:
            return [el for el in self.decorations if el.__class__.__name == decoration_type][0]
        else:
            return 'None'

