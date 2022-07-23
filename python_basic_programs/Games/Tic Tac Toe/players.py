#this is the players file for tic-tac-toe

import math
import random

class Player:
    def __init__(self, letter):
        
        self.letter = letter #this allows us to call a x and an o player
        
    
    def get_move(self, game):
        
        pass #moves game along to next player
        

class ComputerPlayer(Player): #this is for a computer player that inherits base player attributes
    
    def __init__(self, letter):
        
        super().__init__(letter)
        
    def get_move(self, game):
        
        square = random.choice(game.playable_moves()) #this feeds the playable moves in for the computer to choose one
        
        return square #"plays" the move for the computer
    
    
class HumanPlayer(Player):
    
    def __init__(self, letter):
        
        super().__init__(letter)
        
    def get_move(self, game):
        
        playable_square = False #sets playable squares to false
        
        value = None #this is the value input by the user. starts as none because they havent palyed yet
        
        while not playable_square: #provides logic for the game to check for where the player cant play
            
            square = input(self.letter + "\'s turn input move (0-8): ") #pulls input from the user
            
            try: #tries to put input of int into a game square.
                
                value = int(square)
                
                if value not in game.playable_moves(): 
                    
                    raise ValueError #if the square cant be cast to a number then we get an error
                
                playable_square = True
                
            except ValueError: #if we get a value error allows user to try again
                
                print("move invalid please select again")
                
        return value
            

class UnbeatableCompPlayer(Player): #this is logic for a minmax computer player that never loses. 
    
    def __init__(self, letter): 
        
        super().__init__(letter) #same initialization as other palyers
        
    def get_move(self, game): #logic for min max function included
        
        if len(game.playable_moves()) == 9: #if there is no move yet on the board the comp chooses a random place
            
            square = random.choice(game.playable_moves())
            
        else: #uses the moves already played to minmax a way to not lose.
            
            square = self.minimax(game, self.letter) ["position"]#assigns the computer player letter within the game and uses the minimax function logic to return the best posible move  to either win or not lose.
            
        return square #gives the square that is the best possible outcome
    
    def minimax(self, snapshot, player): #each iteration takes a snapshot of the board and applies logic to the computer for its next move
        
        Optimal_player = self.letter #the computer wants to make sure its letter wins!
        
        Opponent_player = "O" if player == "X" else "X" #provides logic for which letter this computer is playing
        
        #move cheks happen here 
        if snapshot.is_winner == Opponent_player: #logic for win condition score calculation
            
            #feed in position of moves and the score for minimax learning
            return {"position" : None, 
                    "score" : 1 * (snapshot.Count_open_Squares() + 1) if Opponent_player == Optimal_player else -1 * (snapshot.Count_open_Squares() + 1)} #creates a dictionary for open squares on the board to get a win state with the most number of open squares left on the board.
            
        elif not snapshot.open_squares(): #if there isnt a winner but empty squares still exist
            
            return {"position" : None,
                    "score" : 0} #score will be 0 (neutral as the win condition has not occured)
        
        #minimax algorithm
        if player == Optimal_player: #if user is Optimal_player( aka trying to win) adds logic for decrimental choices left for optimal play
            
            optimal = {"position" : None, "score" : -math.inf} #lowest score possible is the best as it means that the optimal play was taken at every oportunity
            
        else:
            
            optimal = {"position" : None, "score" : math.inf} #higher score means less open spaces left on the board at win condition.
    
        for valid_move in snapshot.playable_moves(): #creates a simulation of the current game rescursing over all moves utilizing minimax to find best choice for the moves made after.
            
            #steps for logic
            #try a square on the board
            snapshot.make_move(valid_move, player) 
            
            #simulate what the next move could be for a optimal win condition
            simmed_score = self.minimax(snapshot, Opponent_player) #swaps players to sim a gim
            
            #undo that sim and try another
            snapshot.board[valid_move] = " " #sets the simmed move back to an open square
            
            snapshot.is_winner = None #tells if the sim returned a win condition
            
            simmed_score["position"] = valid_move #tells the logic the position ofthe made move
            
            #update the dictionary to see if the made move is the best option
            if player == Optimal_player:
                
                if simmed_score["score"] > optimal["score"]:
                    
                    optimal = simmed_score #gives us the lowest score for our optimal player
            
            else: #sets play for non optimal player
                
                if simmed_score["score"] < optimal["score"]:
                    
                    optimal = simmed_score #gives s the higest score for the person that will lose this game
            
        
        return optimal #returns the dictionary with the best move that can be made that provides the lowest score