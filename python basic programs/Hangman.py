import random
from wordlist import words #this is importing our wordlist from a seperite python file
import string #allows us to get the alphabet letters

def get_usable_word(words): #this fuction takes your list of words and chooses one randomly.
    
    word = random.choice(words)
    
    while '-' in word or ' ' in word: #this while loop makes it so that from our list of words, if it has a space or a - in it we re roll it untill we get a word that doesnt have those as we cant guess them in hangman.
        
        word = random.choice(words)
        
    return word


def Game(): #this is the logic for the game
    
    word = get_usable_word(words)
    
    word_letters = set(word) #allows us to set the letters within words to be guessed.
    
    alphabet = set(string.ascii_uppercase) #gives us the alphabet letters all uppercase.
    
    guessed_letters = set() #this is the variable of letters the user has guessed.
    
    #game loop starts here
    while len(word_letters) > 0:
        
        print("Guessed Letters: ", " ".join(guessed_letters)) #prints the guessed letters in a string seperated by spaces
        
        word_list = [letter if letter in guessed_letters else '-' for letter in word] #shows the word as dashes for each non guessed letter
        
        print("Word your trying to guess: ", " ".join(word_list)) #prints the word that user is trying to guess as dashes.
        
        user_letter = input("guess a letter: ").upper() #takes user input and makes the character uppercase.
    
        if user_letter in alphabet - guessed_letters: #takes the input for a guessed letter and adds it to the set of guessed letters
        
            guessed_letters.add(user_letter)
        
            if user_letter in word_letters:
            
                word_letters.remove(user_letter)
            
        elif user_letter in guessed_letters: #this is for if someone enters the same character more than once.
        
            print("that letter has already been guesed.  try a different one?")
        
        else: #this is for if something other than a letter is entered
        
            print("that character isnt a valid letter.  please try a actual english character")
        
    
    
    
    
user_input = input('please guess a letter: ')