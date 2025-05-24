from card import suits, card_to_tuple

# check if the hand makes a flush (5 cards of the same suit with any rank configuration)
def is_flush(cards):
    shared_suits = [card[1] for card in cards]
    return any(shared_suits.count(suit) >= 5 for suit in suits)

# check if the hand makes a straight (5 cards with ranks in a row ascending)
def is_straight(ranks):
    ranks = sorted(set(ranks))
    # check if there is 5 cards
    if len(ranks) < 5:
        return False
    # check for a special 5 high straight starting from ace
    if ranks[-1] == 14 and 2 in ranks and 3 in ranks and 4 in ranks and 5 in ranks:
        return True
    # check for any straight
    for index in range(len(ranks) - 4):
        if ranks[index + 4] - ranks[index] == 4:
            return True, ranks[index + 4]
    # otherwise there is no straight
    return False

# check overall what hand ranking/combination a player has made
def evaluate_hand(hand, board):
    # setup poker hand notation
    cards = [card_to_tuple(card) for card in hand + board]
    ranks = [card[0] for card in cards]
    suits = [card[1] for card in cards]
    # assign a number counter for each type of hand strength
    rank_count = {}
    for rank in ranks:
        rank_count[rank] = rank_count.get(rank, 0) + 1
    
    # weakest hand combination: a high card
    return (0, max(ranks))

# compare the strengths of two players hands and return number counters instead of booleans for the outcome
def compare_hand(hand_one, hand_two, board):
    # check both hand combinations
    hero = evaluate_hand(hand_one, board)
    villain = evaluate_hand(hand_two, board)
    # compare the hand combinations and return 1 for hero win, -1 for villain win and 0 for a tie
    if hero[0] > villain[0]:
        return 1
    if villain[0] > hero[0]:
        return -1
    if hero[1] > villain[1]:
        return 1
    if villain[1] > hero[1]: 
        return -1
    return 0