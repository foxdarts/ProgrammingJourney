#this is the players file for tic-tac-toe

import math
import random

class Player:
    def __init(self, letter):
        
        self.letter = letter #this allows us to call a x and an o player
        
    
    def get_move(self, game):
        
        pass 
        

class ComputerPlayer(Player): #this is for a computer player that inherits base player attributes
    
    def __init(self, letter):
        
        super().__init(letter)
        
    def get_move(self, game):
        
        square = random.choice(TTTGame.playable_moves()) #this feeds the playable moves in for the computer to choose one
        
        return square #"plays" the move for the computer
    
    
class HumanPlayer(Player):
    
    def __init(self, letter):
        
        super().__init(letter)
        
    def get_move(self, game):
        
        playable_square = False #sets playable squares to false
        
        value = None #this is the value input by the user. starts as none because they havent palyed yet
        
        while not playable_square: #provides logic for the game to check for where the player cant play
            
            square = input(self.letter + "\'s turn input move (0-9): ") #pulls input from the user
            
            try: #tries to put input of int into a game square.
                
                value = int(square)
                
                if value not in tttgame.playable_moves(): 
                    
                    raise ValueError #if the square cant be cast to a number then we get an error
                
                playable_square = True
                
            except ValueError: #if we get a value error allows user to try again
                
                print("move invalid please select again")
                
        return value
            
            