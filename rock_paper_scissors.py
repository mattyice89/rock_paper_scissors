'''
Task: Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays
(using input), compare them, print out a message of congratulations to the
winner, and ask if the players want to start a new game)

Edit:  I'm actually going to build a computer player rather than a second human
player
'''

import random
from sys import exit

choices = ['rock', 'paper', 'scissors']

def choices_function():
    # Select a choice for the computer
    comp_choice = choices[random.randint(0,2)]

    print('Let\'s play a game of Rock, Paper, Scissors')
    print('Please enter "Rock", "Paper", or "Scissors"')

    player_choice = input("> ")

    if player_choice.lower() == comp_choice:
        print(f"Player chose {player_choice} and the computer chose {comp_choice}, please try again.")
        choices_function()
    elif player_choice.lower() == 'rock' and comp_choice == 'paper':
        print(f"Player chose {player_choice} and the computer chose {comp_choice}")
        print("You lose!  Too bad, so sad!")
        play_again()
    elif player_choice.lower() == 'rock' and comp_choice == 'scissors':
        print(f"Player chose {player_choice} and the computer chose {comp_choice}")
        print("Congratulations, you win!")
        play_again()
    elif player_choice.lower() == 'paper' and comp_choice == 'scissors':
        print(f"Player chose {player_choice} and the computer chose {comp_choice}")
        print("You lose!  Too bad, so sad!")
        play_again()
    elif player_choice.lower() == 'paper' and comp_choice == 'rock':
        print(f"Player chose {player_choice} and the computer chose {comp_choice}")
        print("Congratulations, you win!")
        play_again()
    elif player_choice.lower() == 'scissors' and comp_choice == 'rock':
        print(f"Player chose {player_choice} and the computer chose {comp_choice}")
        print("You lose!  Too bad, so sad!")
        play_again()
    elif player_choice.lower() == 'scissors' and comp_choice == 'paper':
        print(f"Player chose {player_choice} and the computer chose {comp_choice}")
        print("Congratulations, you win!")
        play_again()
    else:
        print("Hey dummy, that wasn't one of the choices.  Try again.")
        choices_function()

def play_again():
    print("Do you want to play again? (yes/no)")
    response = input("> ")
    if response.lower() == 'yes':
        choices_function()
    elif response.lower() == 'no':
        print("Ok, thanks for playing!")
        exit()
    else:
        print("That response doesn't make sense, dummy!")
        play_again()

choices_function()
