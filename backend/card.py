# represents cards with their suits and ranks
class Card:
    # spade, heart, diamond, club and numbers from 2 -> T and J -> A (using poker notation)
    rank = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    suit = ['s', 'h', 'd', 'c']

    # card constructor
    def __init__(self, notation: str):
        # for poker notation strings
        rank, suit = notation[0], notation[1]
        self.rank = rank
        self.suit = suit
    
    # card representation ("e.g. As")
    def __repr__(self):
        return f'{self.rank}{self.suit}'