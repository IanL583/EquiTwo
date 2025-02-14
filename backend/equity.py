from card import Card
from hand import Hand
from board import Board
# looping through all possible preflop combinations and outs, as there aren't too many
from itertools import combinations

class Equity:
    # inputs for calculating equity, with hero and villain being terms for player 1 and 2 in heads-up
    def __init__(self, hero: Hand, villain: Hand, board: Board):
        self.hero = hero
        self.villain = villain
        self.board = board
        self.deck = self.create_deck()

    # generate a deck excluding cards from hands and the board
    def create_deck(self):
        deck = {f'{rank}{suit}' for rank in Card.rank for suit in Card.suit}
        seen_cards =  {str(card) for card in self.hero.cards + self.villain.cards + self.board.cards}
        return [Card(card) for card in deck - seen_cards]

    # need to use combinations of 5 hand boards for equity streets and also potential outs
    # calculate pre-flop equity

    # calculate post-flop equity

    # evaluate which hand is stronger with hand rankings

    # return the final equity based on the hand spot

# test outputs
hand_one = Hand("AsAd")
hand_two = Hand("AcAh")
board = Board("2s2d2h")

equity = Equity(hand_one, hand_two, board)
deck = equity.create_deck()
print(deck)