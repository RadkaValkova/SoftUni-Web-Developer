from project.card.card import Card


class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards = []

    def add(self, card: Card):
        if card not in self.cards:
            self.cards.append(card)
            self.count += 1
        else:
            raise ValueError(f'Player {card.name} already exists!')

    def remove(self, card: str):
        current = self.find(card)
        try:
            self.cards.remove(current)
            self.count -= 1
        except ValueError:
            return 'Card cannot be an empty string!'

    def find(self, name: str):
        for card in self.cards:
            if card.name == name:
                return card