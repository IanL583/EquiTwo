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
    def calculate_preflop_equity(self):
        # counters for hero or villain winning, tying, and also board configurations
        hero_wins = 0
        villain_wins = 0
        ties = 0
        boards = 0
        # loop throuugh all the different 5 card board combinations
        for board in combinations(self.deck, 5):
            # increment the board combinations and evaluate the made hands with the board
            boards += 1
            final_board = Board(''.join(map(str, board)))
            winner = self.evaluate_hand_ranking(self.hero, self.villain, final_board)
            # now evaluate the winning or tying scenarios and increment those spots
            if winner == 1:
                hero_wins += 1
            elif winner == -1:
                villain_wins += 1
            else:
                ties += 1
        # return the winning and tying scenarios to the amount of different boards to calculate the equity
        return {
            "Hero Equity": hero_wins / boards * 100,
            "Villain Equity": villain_wins / boards * 100,
            "Tie Equity": ties / boards * 100
        }

    # calculate post-flop equity
    def calcaulte_postflop_equity(self):
        # similar to preflop but it will be 5 - length of the board
        hero_wins = 0
        villain_wins = 0
        ties = 0
        boards = 0
        return 0.0

    # evaluate which hand is stronger with hand rankings
    def evaluate_hand_ranking(self):
        # need poker hand ranking boolean evaluations
        return 1

    # return the final equity based on the type of hand spot
    def calculate_final_equity(self):
        # post or preflop equity based on board
        return 100.0

# test outputs
hand_one = Hand("AsAd")
hand_two = Hand("AcAh")
board = Board("2s2d2h")

equity = Equity(hand_one, hand_two, board)
deck = equity.create_deck()
print(deck)