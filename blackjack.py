# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 20:01:24 2020

@author: joeln
"""

import numpy as np
from random import randint

match_point = 0
bot_match_point = 0
game_ongoing = 1
while game_ongoing == 1:    
    print("Welcome to Joel's Blackjack Game.")
    print("For any feedback, feel free to email me at joelngworks@gmail.com.")
    print("Let's start! To draw, input 1. To pass, input 2.")
    bot_choice_ongoing = 0
    match_ongoing = 1
    player_choice_ongoing = 1
    total_card_drawn = 0
    print("Game has started. It is the player's turn!")
    while player_choice_ongoing == 1:
        print("To draw, input 1. To pass, input 2.")
        print("Type 3 for the rules and 4 for to quit.")
        player_choice = int(input("Your Choice: "))
        if player_choice == 1:
            card_drawn = randint(1, 13)
            if card_drawn == 1:
                print("You have drawn a Ace (1).")
            elif card_drawn == 2:
                print("You have drawn a 2.")
            elif card_drawn == 3:
                print("You have drawn a 3.")
            elif card_drawn == 4:
                print("You have drawn a 4.")
            elif card_drawn == 5:
                print("You have drawn a 5.")
            elif card_drawn == 6:
                print("You have drawn a 6.")
            elif card_drawn == 7:
                print("You have drawn a 7.")
            elif card_drawn == 8:
                print("You have drawn a 8.")
            elif card_drawn == 9:
                print("You have drawn a 9.")
            elif card_drawn == 10:
                print("You have drawn a 10.")
            elif card_drawn == 11:
                print("You have drawn a Jack (10).")
                card_drawn = card_drawn - 1
            elif card_drawn == 12:
                print("You have drawn a Queen (10).")
                card_drawn = card_drawn - 2
            elif card_drawn == 13:
                print("You have drawn a King (10).")
                card_drawn = card_drawn - 3                   
            total_card_drawn = card_drawn + total_card_drawn
            total_card_drawn_text = str(total_card_drawn)
            print(str("Your total hand value is " + total_card_drawn_text))
            if total_card_drawn == 21:
                print("Blackjack! You got 21!")
                print("You can no longer draw but you have won the game.")
                print("Now, watch the dealer self-destruct.")
            if total_card_drawn > 21:
                print("Busted! Your total hand value is more than 21.")
                bot_match_point = bot_match_point + 1
                player_choice_ongoing = 0
                game_ongoing = 0
                match_point_text = str(match_point)
                bot_match_point_text = str(bot_match_point)
                print("Your score is " + match_point_text + " and the dealer's score is " + bot_match_point_text + ".")
                game_ongoing = int(input("Type 1 to continue and 0 to quit."))
        elif player_choice == 2 or total_card_drawn == 21:
             print("The dealer shall now draw.")
             player_choice_ongoing = 0
             bot_choice_ongoing = 1
        elif player_choice == 4:
            player_choice_ongoing = 0
            match_ongoing = 0
            game_ongoing = 0
            match_point_text = str(match_point)
            bot_match_point_text = str(bot_match_point)
            print("Your score is " + match_point_text + " and the banker's score is " + bot_match_point_text + ".") 
        elif player_choice == 3:
            print("Blackjack is a game where the player aims to get a better hand than the dealer.")
            print("The player will first draw cards to his hand and pass when he is ready.")
            print("If the player gets a hand of more than 21, he will go bust.")
            print("If not, the dealer will draw his hand. Likewise the dealer can go bust if he draws more than 21.")
            print("In order to win the game, the player must have a better hand than the dealer.")
        else: 
            player_choice = int(input("Invalid input! Input 1 to continue:  "))
    while bot_choice_ongoing == 1:
        bot_total_drawn = 0
        while bot_total_drawn < total_card_drawn:
            bot_drawn = randint(1, 13)
            if bot_drawn == 1:
                print("The bot has drawn an Ace (1).")
            if bot_drawn == 2:
                print("The bot has drawn a 2.")
            if bot_drawn == 3:
                print("The bot has drawn a 3.")
            if bot_drawn == 4:
                print("The bot has drawn a 4.")
            if bot_drawn == 5:
                print("The bot has drawn a 5.")
            if bot_drawn == 6:
                print("The bot has drawn a 6.")
            if bot_drawn == 7:
                print("The bot has drawn a 7.")
            if bot_drawn == 8:
                print("The bot has drawn a 8.")
            if bot_drawn == 9:
                print("The bot has drawn a 9.")
            if bot_drawn == 10:
                print("The bot has drawn a 10.")
            if bot_drawn == 11:
                print("The bot has drawn a Jack (10).")
                card_drawn = card_drawn - 1
            if bot_drawn == 12:
                print("The bot has drawn a Queen (10).")
                card_drawn = card_drawn - 2
            if bot_drawn == 13:
                print("The bot has drawn a King (10).")
                bot_drawn = card_drawn - 3
            bot_total_drawn = bot_total_drawn + bot_drawn
        total_bot_drawn_text = str(bot_total_drawn)
        print("The player has drawn " + total_card_drawn_text + " while the bot has drawn " + total_bot_drawn_text + " . ")
        if bot_total_drawn > 21:
            print("The dealer has busted! The player wins")
            match_point = match_point + 1
            bot_choice_ongoing = 0
            match_point_text = str(match_point)
            bot_match_point_text = str(bot_match_point)
            print("Your score is " + match_point_text + " and the dealer's score is " + bot_match_point_text + ".")
            game_ongoing = int(input("Type 1 to continue and 0 to quit."))
        else:
            print("The dealer has won with a higher hand!")
            bot_match_point = bot_match_point + 1
            bot_choice_ongoing = 0
            match_point_text = str(match_point)
            bot_match_point_text = str(bot_match_point)
            print("Your score is " + match_point_text + " and the dealer's score is " + bot_match_point_text + ".")    
            game_ongoing = int(input("Type 1 to continue and 0 to quit."))
print("Thanks for playing!")               
