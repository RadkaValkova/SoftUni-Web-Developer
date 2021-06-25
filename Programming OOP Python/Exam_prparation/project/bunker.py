from project.medicine.medicine import Medicine
from project.medicine.painkiller import Painkiller
from project.medicine.salve import Salve
from project.supply.food_supply import FoodSupply
from project.supply.supply import Supply
from project.supply.water_supply import WaterSupply
from project.survivor import Survivor


class Bunker:
    def __init__(self):
        self.survivors = []    # will contain all the survivors (objects)
        self.supplies = []     # will contain all the supplies (objects)
        self.medicine = []

    @property
    def food(self):
        food_sup = [el for el in self.supplies if isinstance(el, FoodSupply)]
        if not food_sup:
            raise IndexError('There are no food supplies left!')
        else:
            return food_sup

    @property
    def water(self):
        water_sup = [el for el in self.supplies if isinstance(el, WaterSupply)]
        if not water_sup:
            raise IndexError('There are no water supplies left!')
        else:
            return water_sup

    @property
    def painkillers(self):
        paink_med = [el for el in self.medicine if isinstance(el, Painkiller)]
        if not paink_med:
            raise IndexError('There are no painkillers left!')
        else:
            return paink_med

    @property
    def salves(self):
        salves_med = [el for el in self.medicine if isinstance(el, Salve)]
        if not salves_med:
            raise IndexError('There are no salves left!')
        else:
            return salves_med

    def add_survivor(self,survivor: Survivor):
        if survivor in self.survivors:
            raise ValueError(f'Survivor with name {survivor.name} already exists.')
        self.survivors.append(survivor)

    def add_supply(self,supply: Supply):
        self.supplies.append(supply)

    def add_medicine(self,medicine: Medicine):
        self.medicine.append(medicine)

    def heal(self, survivor: Survivor, medicine_type: str):
        if survivor.needs_healing:
            if medicine_type == 'Painkillers':
                last_medicine = self.painkillers.pop()
                last_medicine.apply(survivor)
                return f'{survivor.name} healed successfully with {medicine_type}'
            else:
                last_medicine = self.salves.pop()
                last_medicine.apply(survivor)
                return f'{survivor.name} healed successfully with {medicine_type}'

    def sustain(self, survivor: Survivor, sustenance_type: str):
        if survivor.needs_sustenance:
            if sustenance_type == 'Food':
                last_sust = self.food.pop()
                last_sust.apply(survivor)
                return f'{survivor.name} sustained successfully with {sustenance_type}'
            else:
                last_sust = self.water.pop()
                last_sust.apply(survivor)
                return f'{survivor.name} sustained successfully with {sustenance_type}'

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= (2*survivor.age)
            self.sustain(survivor, 'Food')
            self.sustain(survivor, 'Water')

