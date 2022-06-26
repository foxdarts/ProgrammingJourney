import random #random used by functions to select computer inputs


def game(): #game is our function for playing rock, paper, scissors!
    
    user = input("Please enter your pick: 'R' for rock, 'P' for paper, and 'S' for scissors ").lower() #instructs the user for what to enter for their choice
    
    computer = random.choice(['r', 'p', 's']) #computer generates a random choice from the list for comparison
    
    if user == computer:  #rules for RPS r>s, s>p, p>r
        
        return 'Tie! user and random are thinking the same' #this option is if the user and computer both picked the same thing.
    
    if is_won(user, computer): #if function is_won returns true then the user won
        
        return "user wins! take that computer :)"
    
    return "computer wins this one :(" #if it isnt a tie and the user didnt win then the computer won
    
    

def is_won(player, opponent): #rfunction that eturns true if the player wins
    
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        
        return True #this sets it so that if the user inputs a winning entry the function is set to true
    
print(game()) #runs the game in the terminal