#this is a game for tic-tac-toe

import time #just used for a delay between user play and computer play
from players import HumanPlayer, ComputerPlayer #this brings the logic from players into this file.

class TicTacToe:
    def __init__(self):
        
        self.board = [" " for _ in range(9)] #is the list that we will use as our game board.
        
        self.is_winner = None #this is used to keep track of who won
        
        
    def print_board(self):
        
        for row in [self.board[i * 3 : (i + 1) * 3] for i in range(3)]: #this creates and prints the 3 x 3 board for tictactoe
            print('| ' + ' | '.join(row) + ' |') #this sets the "boarder" for the game squares
            
    @staticmethod
    def print_board_numbers(): #statif method to show the options to the user for where they want to play
        
        numbered_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)] #shows the numbers for the rows as they appear in the game board.
        
        for row in numbered_board: 
            
            print('| ' + ' | '.join(row) + ' |') #sets teh borders for the game board so that the numbers for placement render inside
            
    def playable_moves(self): #gives us a function for moves that can be done by the next player
        
        return [i for i, place in enumerate(self.board) if place == " "] #all below code simplified :)
        
        # moves = [] #stores moves in a list
        
        # for (i, place) in enumerate(self.board): #enumerates the places within the board so the logic knows which ones arent taken
            
        #     if place == " ": 
                
        #         moves.append(i) #makes it so that the list of places gets filled with moves as players make them.
                
        # return moves #fills the place on the board
        
    def open_squares(self):
        
        return " " in self.board #sets the empty squares in the board to a bool essentially.
    
    def Count_open_Squares(self):
        
        return self.board.count(" ") #gives us a count of the empty squares left on the board
    
    def make_move(self, square, letter): #gives us the move for a player to a square and the letter for that player.  
        
        if self.board[square] == " ": #if the square is empty
            
            self.board[square] = letter #assign player letter to square
            
            if self.winner(square, letter): #checks if the last move won the game
                
                self.is_winner = letter #declares the last played letter the winner
            
            return True 
            
        else: #otherwise return false. move cant be done
            
            return False
        
        
    def winner(self, square, letter):
        
        row_indexer = square // 3 #checks all rows for win condition
        
        row = self.board[row_indexer * 3 : (row_indexer +1) * 3]
        
        if all([place == letter for place in row]):
            
            return True #logic for row checker
        
        coloum_indexer = square % 3
        
        coloum = [self.board[coloum_indexer + i * 3] for i in range(3)] #checks the coloums for win condition
        
        if all([place == letter for place in coloum]):
            
            return True #logic for couloum checker :)
        
        #check diagonal. check even numbered spaces to see if they equal a win as the board is laid out so that only 0,2,4,6, and 8 are in the corners and center of the board
        
        if square %2 == 0: #if the square is even(aka divisable by 2 with no remainder)
            
            diagonal1 = [self.board[i] for i in [0 , 4 , 8]] #top left to bottom right.
            
            if all([place == letter for place in diagonal1]):
            
                return True
            
            diagonal2 = [self.board[i] for i in [2 , 4 , 6]] #top right to bottom left
            
            if all([place == letter for place in diagonal2]):
            
                return True
        
        return False #this sets if none of the win conditions are met
        
                
def playgame(game, x_player, o_player, print_game_board = True): #gets players.  set print game to false if having computer play computer so it doesnt fill the terminal with game boards each move.
    
    if print_game_board:
        
        game.print_board_numbers() #if print_game_board is true it prints the game board. little logic :)
        
    letter = 'X' #starts the game with a move from x player
    
    
    while game.open_squares(): #loop that plays the game
        
        if letter == "O":
            
            square = o_player.get_move(game) #tells the o player to play
            
        else:
            
            square = x_player.get_move(game) #tells the x player to play
            
        
        if game.make_move(square, letter):
            
            if print_game_board:
                
                print(letter + f" makes a move to square {square}") 
                
                game.print_board() #prints game board with move filled in
                
                print(" ") #provides empty live after game board.
                
            if game.is_winner: #checks for win condition
                
                if print_game_board:
                    
                    print(letter + " is the winner!")
                    
                return letter #prints out winner using last letter palyed
                
            letter = "O" if letter == "X" else "X" #check to see if x or o was palyed and switches players accordingly.
            
        time.sleep(0.5) #adds short time break between user moves and computer move
            
    if print_game_board:
            
        print("it is a tie. no winner this game")
            
            
if __name__ == '__main__': #runs the file
    
    x_player = HumanPlayer("X") #sets the user input to x.
    
    o_player = ComputerPlayer("O") #sets computer player to o.
    
    tgame = TicTacToe() #rums the loops for the game
    
    playgame(tgame, x_player, o_player, print_game_board=True)
    
    
            
        
        