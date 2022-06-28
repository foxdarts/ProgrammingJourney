#this is a game for tic-tac-toe


class TicTacToe:
    def __init__(self):
        
        self.board = [" " for _ in range(9)] #is the list that we will use as our game board.
        
        self.current_winner = None #this is used to keep track of who is winning
        
        
    def print_Board(self):
        
        for row in [self.board[i * 3 : (i + 1) * 3] for i in range(3)]: #this creates and prints the 3 x 3 board for tictactoe
            print('| ' + ' | '.join(row) + ' |') #this sets the "boarder" for the game squares
            
    @staticmethod
    def print_board_numbers(): #statif method to show the options to the user for where they want to play
        
        numbered_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)] #shows the numbers for the rows as they appear in the game board.
        
        for row in numbered_board: 
            
            print('| ' + ' | '.join(row) + ' |') #sets teh borders for the game board so that the numbers for placement render inside
            
    def playable_moves(self): #gives us a function for moves that can be done by the next player
        
        moves = [] #stores moves in a list
        
        for (i, place) in enumerate(self.board): #enumerates the places within the board so the logic knows which ones arent taken
            
            if place == " ": 
                
                moves.append(i) #makes it so that the list of places gets filled with moves as players make them.
                
        return moves #fills the place on the board