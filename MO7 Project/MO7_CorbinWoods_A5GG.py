#!/usr/bin/env python3

import random

def display_title():
    print("Guess the number!")   #welcome message
    print()

def get_limit():
    limit = int(input("Enter the upper limit for the range of numbers: "))  #asks user for input
    return limit

def play_game(limit):
    count = 0
    number = random.randint(1, limit)
    print(f"I'm thinking of a number from 1 to {limit}")  #begins game
   

    while True:
        guess = int(input("Your guess: "))  #asks user for guess
        if guess < number:
            print("Too low.") #if guess is too low, display "Too Low"
            count += 1
        elif guess > number:
            print("Too high.") #If guess is too high, display "Too high"
            count += 1
        elif guess == number:
            print(f"You guessed it in {count} tries.\n") #If guess is correct, display win messge
            return

def main():
    display_title()
    
    again = "y"  #If player selects "y" restart game
    while again.lower() == "y":  #if y is selected, the game will restart.
        limit = get_limit()
        play_game(limit)
        
        again = input("Play again? (y/n): ")  #asks user if they want to restart the game
        print()
    print("Bye!")  #if the user selects "n" or anything other than "y", displays exit message

# if started as the main module, call the main function
if __name__ == "__main__":
    main()

