#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 10:37:05 2018

@author: Chris
"""

import random

suits = ['spades', 'clubs', 'diamonds', 'hearts']
faces = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
hands = []
highest_card = []

print("Enter number of players: ")
NUMBER_OF_PLAYERS = int(input())

for x in range(0, NUMBER_OF_PLAYERS):
    hands.append([])
    for y in range(0, 5):
        hands[x].append([random.choice(faces), random.choice(suits)])
    print("Player %d's hand: " % (x+1) )
    print(hands[x][:])

winning_player = None
winning_card = 2

for x in range(0, NUMBER_OF_PLAYERS):
    for y in range(0, 5):
        rank = faces
        rank.sort(reverse = True)
        for i in rank:
            if hands[x][y][0] >= winning_card:          
                winning_card = hands[x][y][0]
                winning_player = x + 1
                if winning_card == 14:
                    card = "A"
                elif winning_card == 13:
                    card = "K"
                elif winning_card == 12:
                    card = "Q"
                elif winning_card == 11:
                    card = "J"                  
    highest_card.append(card)
    
print("The player with the highest card is player " + str(winning_player)) 
print("Winning card is " + str(card))# poker_game
