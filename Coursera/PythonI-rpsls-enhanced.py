#!/usr/bin/python

# This script will not work outside of the Coursera CodeSkulptor framework (http://www.codeskulptor.org/) 
# since the simplegui module is not natively available for installation/import

# The enhancements to this version of the script include:
#   1) Launches an interactive window with buttons for the player choices
#   2) Keeps a running tally of player and computer wins

import random
import simplegui

# globals

player_wins = 0
comp_wins = 0

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
    elif name == "scissors":
        return 4
    else: 
        print "ERROR: Player selection invalid. Make a valid selection!"

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
    elif number == 4:
        return "scissors"
    else: 
        print "ERROR: Make a valid selection!"

def choose_rock():
    rpsls('rock')

def choose_paper():
    rpsls('paper')

def choose_scissors():
    rpsls('scissors')

def choose_lizard():
    rpsls('lizard')

def choose_spock():
    rpsls('Spock')

        
def rpsls(player_choice):
    '''
    Randomly generates a computer choice from the RPSLS set and compares the 
    translated numerical values of both choices to determine the winner.
    '''
    
    # Define the variables to be used
    global player_wins, comp_wins
    computer_num = random.randrange(0, 5)
    computer_choice = number_to_name(computer_num)
    player_num = name_to_number(player_choice)    
    diff = (player_num - computer_num) % 5

    # Print the choices (this is before the if/else to accommodate the 
    # possibility of a tie, which needs to be handled in the if/else since
    # it doesn't follow the standard format).
    print "Player chooses", player_choice
    print "Computer chooses", computer_choice

    # Compute the winner based on modulated difference between the 
    # numerical values of computer/player choices.
    if diff == 0:
        winner = "tie"
        print "Player and computer tie!"
        print "Score:"
        print "  Player:", player_wins
        print "  Computer:", comp_wins, "\n"
    elif diff <= 2:
        winner = "player"
        player_wins += 1
        print winner.capitalize() + " wins!"
        print "Score:"
        print "  Player:", player_wins
        print "  Computer:", comp_wins, "\n"
    else:
        winner = "computer"
        comp_wins += 1
        print winner.capitalize() + " wins!"
        print "Score:"
        print "  Player:", player_wins
        print "  Computer:", comp_wins, "\n"
    
        
# build the frame structure for player input

frame = simplegui.create_frame('Rock Paper Scissors Lizard Spock', 200, 200)
button1 = frame.add_button('Rock', choose_rock)
button2 = frame.add_button('Paper', choose_paper)
button3 = frame.add_button('Scissors', choose_scissors)
button4 = frame.add_button('Lizard', choose_lizard)
button5 = frame.add_button('Spock', choose_spock)
        
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
#rpsls("rock")
#rpsls("Spock")
#rpsls("paper")
#rpsls("lizard")
#rpsls("scissors")

# always remember to check your completed program against the grading rubric
