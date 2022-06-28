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
        
        pass