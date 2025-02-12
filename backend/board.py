from backend.card import Card

class Board:
    # for multiple boards where we have an empty string then can do 3,4,5 card boards combing ranks and suits
    def __init__(self, notation: str = ""):
        self.cards = [Card(notation[i:i+2]) for i in range(0, len(notation), 2)]
    
    # representing either a 3,4,5 card or empty board by combining cards into strings
    def __repr__(self):
        return " ".join(str(card) for card in self.cards) if self.cards else ""