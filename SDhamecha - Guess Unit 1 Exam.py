#!/usr/bin/env python3
import random

play = "y"
while play == "y":
    # Choose random number from 0 to 10
    random_number = random.randrange(0, 11)
    
    print("Guess the random number in 5 tries!")
    
    tries = 5
    current_try = 1
    won = False
    
    # game loop
    while current_try <= tries and not won:
        guess = int(input(f"Guess #{current_try}. Enter your next guess: "))
        
        if guess == random_number:
            print(f"You guessed the random number: {random_number}")
            print(f"It took you {current_try} tries")
            won = True
        else:
            current_try += 1
            if current_try <= tries:
                print("Sorry that is incorrect, please try again")
                if guess < random_number:
                    print(f"Your guess of {guess} was smaller than the number")
                else:
                    print(f"Your guess of {guess} was bigger than the number")
            else:
                print(f"Sorry, You lose! The number was: {random_number}")
                
    # play again
    play = input("Would you like to play again (y/n): ").lower()
    while play != "y" and play != "n":
        play = input("Invalid input. Enter y or n: ").lower()

print("Completed by, Shivang")