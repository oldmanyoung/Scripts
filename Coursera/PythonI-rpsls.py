#!/usr/bin/python

# A simple script that compares two Rock-Paper-Scissors-Lizard-Spock throws and determins
# the winner (or a tie). The computer throw is determined randomly. The player throw is 
# hard-coded in the test section at the bottom (for now).

import random

# helper functions

def name_to_number(name):
    '''
    Converts the supplied throw name to a corresponding number so winner
    can be calculated.
    '''
    
    # convert name to number using if/elif/else
    # don't forget to return the result!

    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    else: # name == "scissors"
        return 4

def number_to_name(number):
    '''
    Converts the number to a throw name so computer choice can be printed
    as string.
    '''

    # convert number to a name using if/elif/else
    # don't forget to return the result!
    
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    else: # number == 4
        return "scissors"

def rpsls(player_choice):
    '''
    Randomly generates a computer choice from the RPSLS set and compares the 
    translated numerical values of both choices to determine the winner.
    '''
    
    # Define the variables to be used
    computer_num = random.randrange(0, 5)
    computer_choice = number_to_name(computer_num)
    player_num = name_to_number(player_choice)    
    diff = (player_num - computer_num) % 5

    # Print the choices (this is before the if/else to accommodate the 
    # possibility of a tie, which needs to be handled in the if/else since
    # it doesn't follow the standard format).
    print "Player chooses " + player_choice
    print "Computer chooses " + computer_choice

    # Compute the winner based on modulated difference between the 
    # numerical values of computer/player choices.
    if diff == 0:
        winner = "tie"
        print "Player and computer tie!\n"
    elif diff <= 2:
        winner = "player"
        print winner.capitalize() + " wins!\n"
    else:
        winner = "computer"
        print winner.capitalize() + " wins!\n"
    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")


