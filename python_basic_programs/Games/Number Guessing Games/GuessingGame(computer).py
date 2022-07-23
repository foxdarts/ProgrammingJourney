#this is the code for a guessing game where the computer generates a number and the user has to guess it.

import random #imports the random package included in python


def guess(x): #defines the function of guess(the program for the game)
    
    random_num = random.randint(1, x) #starts a random number between 1 and x
    
    guess = 0 #starts teh number the the user is guessing at 0. this makes it imposible for the number to be correct automatically as the computers number is between 1 and x

    
    while guess != random_num: #while loop runs untill the number guessed is the number the computer generated
        guess = int(input(f"guess a Number between 1 and {x} ")) #prompts user for a number between 1 and x
       
        if guess < random_num:
            print("guess is to low. aim higher.") #tells the user if guessed number is to low
            
        elif guess > random_num:
            print("guess again. this time lower.") #tells the user if the guessed number is to high
    
    print(f"yay! you got {random_num} correct!") #prints when the number is guessed correctly.
        

guess(10)

