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
        hero_cards = hero.cards + board.cards
        villain_cards = villain.cards + board.cards
        
        hero_rank = self.get_hand_rank(hero_cards)
        villain_rank = self.get_hand_rank(villain_cards)
        
        if hero_rank[0] > villain_rank[0]:
            return 1  
        elif villain_rank[0] > hero_rank[0]:
            return -1
        else:
            # compare kickers in the case of the same hand ranking
            for h, v in zip(hero_rank[1], villain_rank[1]):
                if h > v:
                    return 1
                elif v > h:
                    return -1
            return 0

    def get_hand_rank(self, cards):
        ranks = sorted([Card.rank.index(card.rank) for card in cards], reverse=True)
        suits = [card.suit for card in cards]
        rank_counts = {}
        for r in ranks:
            rank_counts[r] = rank_counts.get(r, 0) + 1
        
        # check for flush
        suit_counts = {}
        for s in suits:
            suit_counts[s] = suit_counts.get(s, 0) + 1
        is_flush = max(suit_counts.values()) >= 5
        
        # check for straight
        unique_ranks = sorted(set(ranks), reverse=True)
        is_straight = False
        for i in range(len(unique_ranks) - 4):
            if unique_ranks[i] - unique_ranks[i + 4] == 4:
                is_straight = True
                straight_high = unique_ranks[i]
                break

        # check for low straight 
        if 12 in ranks and 0 in ranks and 1 in ranks and 2 in ranks and 3 in ranks:
            is_straight = True
            straight_high = 3
        
        # get rank frequencies
        count_values = sorted(rank_counts.values(), reverse=True)
        rank_by_count = sorted(rank_counts.items(), key=lambda x: (-x[1], -x[0]))
        
        # hand rankings from highest to lowest 
        if is_flush and is_straight and straight_high == 12:
            return (9, [12])  # Royal Flush
        elif is_flush and is_straight:
            return (8, [straight_high])  # Straight Flush
        elif count_values[0] == 4:
            return (7, [rank_by_count[0][0]])  # Four of a Kind
        elif count_values[0] == 3 and count_values[1] == 2:
            return (6, [rank_by_count[0][0], rank_by_count[1][0]])  # Full House
        elif is_flush:
            flush_ranks = sorted([r for i, r in enumerate(ranks) 
                                if suits[i] in [s for s in suit_counts if suit_counts[s] >= 5]], 
                                reverse=True)
            return (5, flush_ranks[:5])  # Flush
        elif is_straight:
            return (4, [straight_high])  # Straight
        elif count_values[0] == 3:
            kickers = [r for r, c in rank_by_count[1:] if c == 1][:2]
            return (3, [rank_by_count[0][0]] + kickers)  # Three of a Kind
        elif count_values[0] == 2 and count_values[1] == 2:
            kickers = [r for r, c in rank_by_count[2:] if c == 1][:1]
            return (2, [rank_by_count[0][0], rank_by_count[1][0]] + kickers)  # Two Pair
        elif count_values[0] == 2:
            kickers = [r for r, c in rank_by_count[1:] if c == 1][:3]
            return (1, [rank_by_count[0][0]] + kickers)  # One Pair
        else:
            return (0, ranks[:5])  # High Card

# test outputs for debugging
hand_one = Hand("AsAd")
hand_two = Hand("AcAh")
board = Board("2d2c2s")

equity = Equity(hand_one, hand_two, board)
print(equity.calculate_equity())