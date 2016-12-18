#!/usr/bin/python

# "Guess the number" mini-project (with enhancements)
# Input will come from buttons and an input field
# All output for the game will be printed in the simplegui console
# NOTE: Simplegui will only work in the CodeSkulptor environment
# www.codeskulptor.org

# Import required modules
import random
import math
import simplegui

# Define globals
secret_number = random.randrange(0, 100)
range_top = 100
max_guesses = int(math.ceil(math.log(range_top, 2)))
rem_guesses = max_guesses
actual_guesses = 0

# define the helper functions
def new_game():
    ''' Begins a new game, resetting certain global variables '''
#    print secret_number	# for quick debugging purposes
    reset_globals()
    print "I'm thinking of a number between 0 and", range_top, ". See if \nyou can guess it. You have", max_guess_calc(range_top), "guesses remaining.\n"
    
def max_guess_calc(number):
    ''' 
    Calculates the max # of guesses based on the top of the range
    using the logX-base2 formula. Rounds that number up and converts
    to integer.
    '''
    return int(math.ceil(math.log(number, 2)))
    
def is_valid(guess):
    '''
    Determine if the user-input is valid. To be valid, it must be 
    an integer within the range (inclusive) of the game being played.
    For example, if the game is a 0-100 game, valid guesses are only 
    integers in the set {0..100}. Converts the valid range of integers
    to string first for like-to-like comparison.
    '''
    if guess in str(range(0, range_top + 1)):
        return True
    else:
        return False

def reset_globals():
    '''
    This resets several of the global variables, which is necessary 
    to begin a new game after completing an existing one (else the 
    secret # stays the same and max_guesses remains at previous, 
    decremented, value).
    '''
    global secret_number, max_guesses, actual_guesses, rem_guesses
    secret_number = random.randrange(0, range_top)
    max_guesses = int(math.ceil(math.log(range_top, 2)))
    rem_guesses = max_guesses
    actual_guesses = 0
    
def scorecard(actual_guesses):
    '''
    In the event that the secret number is guessed, this function
    returns the success message, tailored to the 'proficiency' of 
    the guesser.
    '''
    if actual_guesses == max_guesses:
        print "That's my number! In the nick of time too. It took you",actual_guesses,"guesses.\n(Were you nervous?)"
    elif actual_guesses == max_guesses - 1:
        print "That's my number! Not bad...It took you",actual_guesses,"guesses.\n(A little luck on your side?)"
    elif actual_guesses == 1:
        print "That's my number! HOLE IN ONE! It only took you",actual_guesses,"guess!\n(Time to play the lottery?)"
    else:
        print "That's my number! Very impressive! It only took you",actual_guesses,"guesses.\n(You've played this before haven't you?)"
    
# define event handlers for control panel
def range100():
    ''' 
    button that changes the range to [0,100) and starts a new game 
    '''
    global secret_number, range_top, max_guesses, rem_guesses
    secret_number = random.randrange(0, 100)
    range_top = 100
    max_guesses = max_guess_calc(range_top)
    rem_guesses = max_guesses
    new_game()
    
def range1000():
    ''' 
    button that changes the range to [0,1000) and starts a new game 
    '''
    global secret_number, range_top, max_guesses, rem_guesses
    secret_number = random.randrange(0, 1000)
    range_top = 1000
    max_guesses = max_guess_calc(range_top)
    rem_guesses = max_guesses
    new_game()

# define the main function for the game
def input_guess(guess):
    '''
    The logic is a number of nested conditionals. The outermost first
    checks to see if the player guess is valid. Next check compares the guess
    to the secret number and returns an appropriate response. The next
    conditional checks to see if the guesses have run out.
    '''
    global max_guesses, secret_number, actual_guesses, rem_guesses
    if is_valid(guess):
        guess = int(guess)
        if guess < secret_number:
            print "You guessed", str(guess),"...too LOW. Guess again!"
            rem_guesses -= 1
            actual_guesses += 1
            if rem_guesses == 0:
                print "Doh! That was your last guess! Try again?\n"
                new_game()
            else:	
                print "You have", str(rem_guesses), "remaining...\n"
        elif guess > secret_number:
            print "You guessed", str(guess),"...too HIGH. Guess again!"
            rem_guesses -= 1
            actual_guesses += 1
            if rem_guesses == 0:
                print "Doh! That was your last guess! Play again?\n"
                new_game()
            else:	
                print "You have", str(rem_guesses), "remaining...\n"
        else:
            actual_guesses += 1
            scorecard(actual_guesses)
            print "Play again!\n"
            new_game()
    else:
            print "Uh, sorry, that's not a valid number...\n"
            
# create frame with an input field and two buttons for the two game types
frame = simplegui.create_frame('Guess the number', 200, 200, 200)
inp = frame.add_input('Enter your guess', input_guess, 50)
button1 = frame.add_button('Start a new game! (Secret number between 0 and 100)', range100)
button1 = frame.add_button('Start a new game! (Secret number between 0 and 1000)', range1000)

# register event handlers for control elements and start frame
frame.start()

# call new_game 
new_game()

