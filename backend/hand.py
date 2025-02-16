from card import Card

class Hand:
    def __init__(self, notation: str):
        # create a notation thats like "e.g. AsKd"
        self.cards = [Card(notation[:2]), Card(notation[2:])]

    def __repr__(self):
        # represent the two cards together to form a hand
        return f'{self.cards[0]}{self.cards[1]}'