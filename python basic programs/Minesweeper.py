#this is a command line version of minesweer.

import random 


class GameBoard: #creates a class for the gameboard.
    
    def __init__(self, Board_size, BombNumber):
        
        self.Board_size = Board_size #assigns the board size to the class
        
        self.BombNumber = BombNumber #assigns the number of bombs to the class
        
        
        #board creation
        self.GBoard = self.create_new_board() #used to create a board with unmarked mines
        
        self.Spot_Values()
        
        #tuple storage for tracking locations and open spaces
        self.dug = set()
        
        
    def create_new_board(self):
        #generates a list of lists using the board size
        
        
        #actually generate the board
        GBoard = [[None for _ in range(self.Board_size)] for _ in range(self.Board_size)] #creates a list of board size long and board size high
        
        #planting the bombs
        HiddenBombs = 0 #variable for hidden bombs
        
        while HiddenBombs < self.BombNumber: #while the number of hidden bombs is less than the number of bombs that are going to be on the board, do this stuff
            
            HideSpot = random.randint(0, self.Board_size ** 2 -1) #generates a random number within the board for the bombs to get placed.
            
            hiderow = HideSpot // self.Board_size #provides the row for where a bomb was put

            hidecol = HideSpot % self.Board_size #provides the coloum for where the bomb was put
            
            if GBoard[hiderow][hidecol] == '*': #if there is already a bomb at that space find another place.
                
                continue
            
            GBoard[hiderow][hidecol] = "*" #plant a bomb in the empty space
            
            HiddenBombs += 1 #incriments the bomb number then repeat untill bombnumber is reached
            
        return GBoard #feeds in the board with the bombs planted on it
        
        
    def Spot_Values(self): 
        #gives us values for the spaces on the board based on how many bombs are next to each spot.
        
        for r in range(self.Board_size): #for each row in the board
            
            for c in range(self.Board_size): #and each coloum
                
                if self.GBoard[r][c] == "*": #if there is a bomb
                    
                    Continue #dont do anything
                
                self.GBoard[r][c] = self.Display_neighbor_bomb(r, c) #if there isnt a bomb tell us how many bombs are touching this spot
                
    
    def Display_neighbor_bomb(self, hiderow, hidecol): 
        #provides us the function to show neighboring bombs to each spot
        #must check each spot around the spot we are checking making sure that if the spot is on the side of the board we dont count anything for those spaces that are "off" the game board
        
        adjacent_bombs = 0 #variable for the adjacent bombs
        
        for r in range(max(0, hiderow - 1), min(self.Board_size - 1, hiderow + 1) + 1): #scans every spot in each row around a spot with checks for out of bounds
            
            for c in range(max(0, hidecol - 1), min(self.Board_size - 1, hidecol +1) + 1): #scans each coloum spot around each spot with check for out of bounds
                
                if r == hiderow and c == hidecol: #this is the spot we are checking around
                    
                    continue #do nothing cause we are checking for adjacent bombs
                
                if self.GBoard[r][c] == "*": #if there is a bomb in an adjacent square
                    
                    adjacent_bombs +=1 #add one to the adjeacnet bomb counter
                
        return adjacent_bombs #feeds the numbers into the board
        
    def dug(self, hiderow, hidecol):
        #takes user input for digging, return safe if no explode, returns game over message if dug = bomb
        
        #bomb hit
        
        #spot with adjacent bomb
        
        #spot with nothing - dig till adjacent bomb is found
        
        self.dug.add((hiderow, hidecol)) #keeps track of where the user has dug
        
        #bomb hit
        if self.GBoard[hiderow][hidecol] == "*":
            
            return False #there was a bomb here
        
        #spot with adjacent bomb
        elif self.GBoard[hiderow][hidecol] > 0:
            
            return True #didnt dig up a bomb

        #spot with nothing - dig till adjacent bomb is found
        for r in range(max(0, hiderow - 1), min(self.Board_size - 1, hiderow + 1) + 1): #scans every spot in each row around a spot with checks for out of bounds
            
            for c in range(max(0, hidecol - 1), min(self.Board_size - 1, hidecol +1) + 1): #scans each coloum spot around each spot with check for out of bounds 
                
                if (r, c) in self.dug: 
                    
                    continue #means the spot you are trying to dig has already been dug
                
                self.dug(r, c) #otherwise add it to your dug list.
                
                                
        
                
        return True
                
    def __str__(self): #magic happens here!
        #this is what actually prints out the board so that the user can see it.
        
        #board of what the user sees
        VisibleBoard = [[None for _ in range(self.Board_size)] for _ in range(self.Board_size)] #generates a blank board given the states board size
        
        for hiderow in range(self.Board_size): #generates rows
            
            for hidecol in range(self.Board_size): #generates coloums
                
                if (hiderow, hidecol) in self.dug: #tests for dug spots
                    
                    VisibleBoard[hiderow][hidecol] = str(self.GBoard[hiderow][hidecol]) #assigns dug spots to the visible board for the user
                    
                else:
                    
                    VisibleBoard[hiderow][hidecol] = " " #sets spaces not dug out to be blank space
                    
        
        


#game function
def PlayGame(Board_size = 20, BombNumber = 5): #board size will determine hopw many spaces are along each axis.  bombnumber sets the number of random bombs within that board space.
    
    #board build goes here
    GBoard = GBoard(Board_size, BombNumber)
    
    
    #board printing and asking for input goes here
    
    
    
    #bomb location and recursion searching goes here with messages for game over nd eventual victory.
    
    pass