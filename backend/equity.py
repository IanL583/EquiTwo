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
        hero_wins = 0
        villain_wins = 0
        ties = 0
        boards = 0
        remaining_cards = 5 - len(self.board.cards)
        for board in combinations(self.deck, remaining_cards):
            boards += 1
            board_str = ''.join(str(self.board).split()) + ''.join(map(str, board))
            final_board = Board(board_str)
            winner = self.evaluate_hand_ranking(self.hero, self.villain, final_board)
            if winner == 1:
                hero_wins += 1
            elif winner == -1:
                villain_wins += 1
            else:
                ties += 1
        hero_equity = round(hero_wins / boards * 100, 2)
        villain_equity = round(villain_wins / boards * 100, 2)
        tie_equity = round(ties / boards * 100, 2)
        return {
            "Hero Equity": hero_equity,
            "Villain Equity": villain_equity,
            "Tie Equity": tie_equity
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

if __name__ == "__main__":
    # test outputs for debugging
    hand_one = Hand("AsKd")
    hand_two = Hand("QdAh")
    board = Board("2d2c2s")
    equity = Equity(hand_one, hand_two, board)
    print(equity.calculate_equity())