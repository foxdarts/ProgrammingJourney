#this program has the computer try to guess a number that the user is thinking of

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
        
        
def computers_guess(x): #code for having the computer guess a number that we are thinking of
    
    lownum = 1
    highnum = x
    feedback = '' #this is the user input to tell the computer if the guess is high, low, or correct
    
    while feedback != 'c': #sets c as the way to tell the computer it guessed correctly
        
        if lownum != highnum: #this ensures that the random set variables cant be set to the same number
            
            guess = random.randint(lownum, highnum)
            
        else:
            
            guess = lownum #could also be set to high
        
        feedback = input(f"is {guess} to high? (H), too low? (L), or correct? (C) ").lower() #this is the code that lets the user know what to enter to tell the computer which direction to move its guess
        
        if feedback == "h":
            
            highnum = guess -1 #means the guess was to high
            
        if feedback == "l":
            
            lownum = guess +1 #means the guess was to low
            
    print(f"the computer guessed {guess} correctly!!")


computers_guess(10)

