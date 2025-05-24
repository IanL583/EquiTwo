from card import deck
from hand import compare_hand
import random

def calculate_equity(hand_one, hand_two, board):
    return {
        'Hero Win': 0.0,
        'Hero Tie': 0.0,
        'Villain Win': 0.0,
        'Villain Tie': 0.0
    }