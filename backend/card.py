# represents cards and representation with their ranks and suits
# spade, heart, diamond, club and numbers from 2 -> T and J -> A (using poker notation)
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
suits = ['s', 'h', 'd', 'c']
rank_values = {rank: index + 2 for index, rank in enumerate(ranks)}

# using poker notation such as As for ace of spades to form a 52 card deck
deck = [rank + suit for rank in ranks for suit in suits]

# create a tuple of poker hands
def card_to_tuple(card):
    return (rank_values[card[0], card[1]])
