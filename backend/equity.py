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

    # calculate the equity of two hands based on the board state
    def calculate_equity(self):
        # counters for winning scenarios for the hero or the villain or ties with different potential boards
        hero_wins = 0
        villain_wins = 0
        ties = 0
        boards = 0
        # get cards needed to complete the board from either preflop, flop, turn or river
        remaining_cards = 5 - len(self.board.cards)
        for board in combinations(self.deck, remaining_cards):
            boards += 1
            # create final board using outs
            final_board = Board(str(self.board) + ''.join(map(str, board)))
            # get the winner of each board and increment the counters
            winner = self.evaluate_hand_ranking(self.hero, self.villain, final_board)
            if winner == 1:
                hero_wins += 1
            elif winner == -1:
                villain_wins += 1
            else:
                ties += 1
        # return the equity percentages
        return {
            "Hero Equity": hero_wins / boards * 100,
            "Villain Equity": villain_wins / boards * 100,
            "Tie Equity": ties / boards * 100
        }

    # evaluate which hand is stronger with hand rankings
    def evaluate_hand_ranking(self, hero: Hand, villain: Hand, board: Board):
        # need poker hand ranking boolean evaluations
        return 1

# test outputs for debugging
hand_one = Hand("AsAd")
hand_two = Hand("AcAh")
board = Board("2d2c2s")

equity = Equity(hand_one, hand_two, board)
deck = equity.create_deck()
print(deck)