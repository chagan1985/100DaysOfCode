###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 11 project - Christopher Hagan
#
###################################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def dealCard():
    return random.choice(cards)

def currentScore(cards_list):
    score = sum(cards_list)
    if score > 21 and 11 in cards_list:
        cards_list.remove(11)
        cards_list.append(1)
        score = sum(cards_list)
    return score

def decideWinner(players_final_score, dealers_final_score):
    if players_final_score > 21:
        print('You bust, you lose!')
    elif dealers_final_score > 21:
        print('The dealer bust, you win!')
    elif players_final_score > dealers_final_score:
        print('You won, congratulations!')
    elif players_final_score < dealers_final_score:
        print('You lost, commiserations')
    else:
        print('Draw')


play_again = True
while play_again:
    player_cards = []
    dealer_cards = []
    if input("Do you want to play a game of blackjack? Type 'y' or 'n': ").lower().startswith('y'):
        print(logo)
        for i in range(2):
            player_cards.append(dealCard())
            dealer_cards.append(dealCard())
        
        dealers_score = currentScore(dealer_cards)
        end_turn = False
        while not end_turn:
            players_score = currentScore(player_cards)

            print('\tYour cards {}, current score: {}'.format(player_cards, players_score))
            print("\tDealer's first card: {}".format(dealer_cards[0]))

            if currentScore(player_cards) < 21 and input("Type 'y' to get another card, type 'n' to pass: ").lower().startswith('y'):
                player_cards.append(dealCard())
            else:
                end_turn = True

        while dealers_score < 17:
            dealer_cards.append(dealCard())
            dealers_score = currentScore(dealer_cards)

        print('\tYour final hand {}, final score: {}'.format(player_cards, players_score))
        print("\tDealer's final hand: {}, final score: {}".format(dealer_cards, dealers_score))
        decideWinner(players_score, dealers_score)

    else:
        play_again = False
