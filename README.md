# EquiTwo
A Heads-up Poker Equity Calculator with or without a Board written in Python

This will be a display of all the possible poker cards in a deck with two slots for two hands.
There will also be 5 slots for the cards in the board and have an option to calculate the equity, which is the chance a hand wins or ties at different stages.
These stages, include having two hands at preflop (an empty board), flop (3 cards on the board), turn (4 cards on the board), and the river (5 cards on the board).

Planning:
- create a deck with lists
- then form all possible hands
- compute all possible boards using an iterator with hand rankings so we can calculate preflop equities
- then we can just easily calculate post flop equities by judging the number of outs 
- style it so we can see all possbile cards in the deck, both hands, and also the board

make sure to organise code, consistent style and naming, use git, use package mangers and virutal environments, comment, unit test, and finally deploy!