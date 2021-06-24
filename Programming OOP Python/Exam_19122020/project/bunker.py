class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []
        # self.__food = []
        # self.__water = []
        # self.__painkillers = []
        # self.__salves = []

    @property
    def food(self):
        foods = [s for s in self.supplies if s.__class__.__name__ == 'FoodSupply']
        if not foods:
            raise IndexError("There are no food supplies left!")
        return foods
        # try:
        #     [el for el in self.supplies if el.__class__.__name__ == 'FoodSupply']
        # except IndexError:
        #     return 'There are no food supplies left!'

    @property
    def water(self):
        water = [s for s in self.supplies if s.__class__.__name__ == 'WaterSupply']
        if not water:
            raise IndexError("There are no water supplies left!")
        return water
        # try:
        #     [el for el in self.supplies if el.__class__.__name__ == 'WaterSupply']
        # except IndexError:
        #     return 'There are no water supplies left!'

    @property
    def painkillers(self):
        painkiller = [s for s in self.medicine if s.__class__.__name__ == 'Painkiller']
        if not painkiller:
            raise IndexError("There are no painkillers left!")
        return painkiller
        # try:
        #     [el for el in self.medicine if el.__class__.__name__ == 'Salve']
        # except IndexError:
        #     return 'There are no water supplies left!'

    @property
    def salves(self):
        salve = [s for s in self.medicine if s.__class__.__name__ == 'Salve']
        if not salve:
            raise IndexError("There are no salves left!")
        return salve
        # try:
        #     [el for el in self.medicine if el.__class__.__name__ == 'Painkiller']
        # except IndexError:
        #     return 'There are no water supplies left!'

    def add_survivor(self, survivor):
        if survivor in self.survivors:
            raise ValueError(f'Survivor with name {survivor.name} already exists.')
        self.survivors.append(survivor)
        # if survivor not in self.survivors:
        #     self.survivors.append(survivor)
        # else:
        #     raise ValueError(f'Survivor with name {survivor.name} already exists.')

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def heal(self, survivor, medicine_type: str):
        if survivor.needs_healing:
            if medicine_type == "Salve":
                current = self.salves.pop()
            else:
                current = self.painkillers.pop()
            self.medicine.remove(current)
            current.apply(survivor)
            return f"{survivor.name} healed successfully with {medicine_type}"
        return

    # def heal(self, survivor, medicine_type: str):
    #     med = None
    #     if survivor.needs_healing:
    #         for el in reversed(self.medicine):
    #             if el.__class__.__name__ == medicine_type:
    #                 med = el
    #                 list(reversed(self.medicine)).remove(el)
    #     med.apply(survivor)
    #     return f'{survivor.name} healed successfully with {medicine_type}'

    def sustain(self, survivor, sustenance_type: str):
        if survivor.needs_sustenance:
            if sustenance_type == "FoodSupply":
                current = self.food.pop()
            else:
                current = self.water.pop()
            self.supplies.remove(current)
            current.apply(survivor)
            return f"{survivor.name} sustained successfully with {sustenance_type}"
        return

    # def sustain(self, survivor, sustenance_type: str):
    #     sust = None
    #     if survivor.needs_sustenance:
    #         for el in reversed(self.supplies):
    #             if el.__class__.__name__ == sustenance_type:
    #                 sust = el
    #                 list(reversed(self.supplies)).remove(el)
    #     sust.apply(survivor)
    #     return f'{survivor.name} sustained successfully with {sustenance_type}'

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= (survivor.age * 2)
            self.sustain(survivor, 'FoodSupply')
            self.sustain(survivor, 'WaterSupply')



