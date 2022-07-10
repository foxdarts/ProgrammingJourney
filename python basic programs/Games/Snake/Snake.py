#this is python file for creating the classic snake game using object orientation and tkinter gfor the gui!


import math #math is important!
import random #random is used for random things
import pygame #pygame lets us create a game board and paly
import tkinter as tk #tkinter is used for gui
from tkinter import messagebox #and alert boxes.


#board creation and stuff

class box(object):
    
    rows = 20 #rows x rows in the board
    
    pixels = 500 #game board pixels
    
    def __init__(self, start, dirnx = 1, dirny = 0, color = (255, 0, 0)): #where the snake will start and original direction
        
        self.position = start #starts the snake box object at its starting point
        
        self.dirnx = 1 #starts movement of snake
        
        self.dirny = 0
        
        self.color = color #makes the snake boxes a certain color
    
    def movement(self, dirnx, dirny): #for movement of the snake
        
        self.dirnx = dirnx
        
        self.dirny = dirny
        
        self.position = (self.position[0] + self.dirnx, self.position[1] + self.dirny) #makes the snake movement but treats just generate as they have no movement vector
    
    def draw(self, board, eyes = False): #generates boxes on the board
        
        distance = self.pixels // self.rows
        
        i = self.position[0] #position in rows
        
        j = self.position[1] #position in coloums
        
        pygame.draw.rect(board, self.color, (i * distance + 1, j * distance + 1, distance -2, distance -2)) #sets the created box's smaller than the game grid so the game grid remains visible.
        
        #eyes for the snake
        if eyes:
            
            center = distance // 2 #makes center half the distance to the edge of a box
            
            radius = 3 #pixel measure
            
            EyeMiddle = (i * distance + center - radius, j * distance + 8) #eye 1
            
            EyeMiddle2 = (i * distance + distance - radius * 2, j * distance + 8) #eye 2
            
            pygame.draw.circle(board, (0, 0, 0), EyeMiddle, radius)
            
            pygame.draw.circle(board, (0, 0, 0), EyeMiddle2, radius)
    

class Snake(object): #snake!

    body = [] #list of boxes used as snake body
    
    turns = {} #set for which direction the snake can turn

    def __init__(self, color, position): #snake object
        
        self.color = color #colors snake the snake color
        
        self.head = box(position) #makes the head of the snake a specific box on the board
        
        self.body.append(self.head) #used to add to the snake body
        
        self.dirnx = 0 #direction snake is going in x direction
        
        self.dirny = 1 #direction snake is going in y direction
    
    def movement(self): #snake movement
        
        for event in pygame.event.get(): #listens for inputs on the gameboard

            if event.type == pygame.QUIT:
                
                pygame.quit() #if the window is closed, stop running the game
                
            keys = pygame.key.get_pressed() #gives a list of direction inputs
            
            for key in keys: #clarifies key inputs
                
                if keys[pygame.K_LEFT]: #if left is pressed
                    
                    self.dirnx = -1 #sets movement to going left
                    
                    self.dirny = 0
                    
                    self.turns[self.head.position[:]] = [self.dirnx, self.dirny] #writes teh spot that the movement happened so snake body can follow that path.
                    
                elif keys[pygame.K_RIGHT]: #if right is pressed
                    
                    self.dirnx = 1 #sets movement to going right
                    
                    self.dirny = 0
                    
                    self.turns[self.head.position[:]] = [self.dirnx, self.dirny] #writes teh spot that the movement happened so snake body can follow that path.
                    
                elif keys[pygame.K_UP]: #if up is pressed
                    
                    self.dirnx = 0 #sets movement to going up
                    
                    self.dirny = -1
                    
                    self.turns[self.head.position[:]] = [self.dirnx, self.dirny] #writes teh spot that the movement happened so snake body can follow that path.
                    
                elif keys[pygame.K_DOWN]: #if down is pressed
                    
                    self.dirnx = 0 #sets movement to going down
                    
                    self.dirny = 1
                    
                    self.turns[self.head.position[:]] = [self.dirnx, self.dirny] #writes teh spot that the movement happened so snake body can follow that path.
                    
        for i, b in enumerate(self.body): #for each box on the snake
            
            p = b.position[:] #get the position of it
            
            if p in self.turns: #see if position is in turns set
                
                turn = self.turns[p]
                
                b.movement(turn[0], turn[1]) #turn the snake at the box where the input was taken
                
                if i == len(self.body) -1:
                    
                    self.turns.pop(p) #once snake body leaves the turn. remove that list so u dont run into ghost blocks.
                    
            else:
                
                if b.dirnx == -1 and b.position[0] <= 0: b.position = (b.rows -1, b.position[1]) #if at left edge of screen continue at position on right edge
                
                elif b.dirnx == 1 and b.position[0] >= b.rows - 1: b.position = (0, b.position[1]) #if at right edge of screen etc
                
                elif b.dirny == 1 and b.position[1] >= b.rows - 1: b.position = (b.position[0], 0) #if at top of screen etc
                
                elif b.dirny == -1 and b.position[1] <= 0: b.position = (b.position[0], b.rows - 1) #if at bottom of screen etc
                
                else: #can movement freely in direction already moving
                    
                    b.movement(b.dirnx, b.dirny) #keep moving that direction
    

    
    def reset(self, position): #reset on death
        
        self.head = box(position) #starts at base position
        
        self.body = [] #emptys added parts list
        
        self.body.append(self.head) #resets head
        
        self.turns = {} #clears turn list
        
        self.dirnx = 0 #starting direction
        
        self.dirny = 1 #starting direction
    
    def addpart(self): #grow when eating treat
        
        tail = self.body[-1] #adds tail to back of snake head
        
        dx = tail.dirnx #variable to keep track of where tail is on x
        
        dy = tail.dirny #variable for where tail is on y
        
        #movement checking to ensure box is added to correct side and follows snake head
        if dx == 1 and dy == 0: #if moving right add to left
            
            self.body.append(box((tail.position[0] - 1, tail.position[1])))
            
        elif dx == -1 and dy ==0: #if moving left add to right
            
            self.body.append(box((tail.position[0] + 1, tail.position[1])))
            
        elif dx == 0 and dy == 1: #if moving up add to bottom
            
            self.body.append(box((tail.position[0], tail.position[1] - 1)))
            
        elif dx == 0 and dy == -1: #if moving down add to top
            
            self.body.append(box((tail.position[0], tail.position[1] + 1)))
            
        self.body[-1].dirnx = dx #makes the added part move with the snake in x
        
        self.body[-1].dirny = dy #makes added part stay with snake movement
            
        
    
    def draw(self, board): #draws the body
        
        for i, b in enumerate(self.body):
            
            if i == 0:
                
                b.draw(board, True) #gives the first snake box eyes
                
            else:
                
                b.draw(board) #draws snake boy


def drawSquares(pixels, rows, board): #displays the game board
    
    Gap =   pixels // rows #calculation for gap space between quares on the board
    
    x = 0 #variable for drawing the game board in the game window
    
    y = 0 #see x comment
    
    for l in range(rows): # 
        
        x = x + Gap
        
        y = y + Gap
        
        pygame.draw.line(board, (255, 255, 255), (x, 0), (x,    pixels))
        
        pygame.draw.line(board, (255, 255, 255), (0, y),    (pixels, y))

def RedrawSquares(board): #refreshes the board on treat place
    
    global width, rows, GSnake, Treat
    
    board.fill((0, 0, 0))
    
    GSnake.draw(board)
    
    Treat.draw(board) 
    
    drawSquares(width, rows, board)
    
    pygame.display.update()

def RandomTreat(rows, item): #random placement of treats to be eaten
    
    placement = item.body
    
    while True:
        
        x = random.randrange(rows)
        
        y = random.randrange(rows)
        
        if len(list(filter(lambda z:z.position == (x, y), placement))) > 0: #checks for snake body to ensure that it isnt placing a treat on a body part.
            
            continue #run loop again
        
        else:
            
            break #place treat
        
    return (x,y) #place treat at position
            
def Message_box(Title, Message): #message box for death
    
    root = tk.Tk() #generates a tkinter message box
    
    root.attributes('-topmost', True) #puts it on top of all other windows
    
    root.withdraw() #makes it invisible!
    
    messagebox.showinfo(Title, Message) #feeds heading and message into tkinter box
    
    try:
        
        root.destroy() #if the box doesnt display destroys the tkinter box
        
    except:
        
        pass #otherwise shows the box


def main(): #main game running
    
    global width, rows, GSnake, Treat
    
    width = 500 #variable for game board dimencions
    
    rows = 20 #sets number of rows on game board

    GBoard = pygame.display.set_mode((width, width))
    
    GSnake = Snake((255,0,0), (10,10))  #sets the color of the snake to red and its starting position to the middle of the board
    
    Treat = box(RandomTreat(rows, GSnake), color = (0, 255, 0)) #generates a treat on the board.

    Running = True #forces flag to start in the true state meaning the game is running
    
    clock = pygame.time.Clock() #internal pygame clock
    
    
    while Running: #game loop starts here
        
        pygame.time.delay(50) #sets a 50 millisecond delay to the game start
        
        clock.tick(10) #locks the gamr to running at 10 frames a second
        
        GSnake.movement() #allows the snake to movement
        
        if GSnake.body[0].position == Treat.position: #if the snake head gets a treat
            
            GSnake.addpart() #add a part to the snake
            
            Treat = box(RandomTreat(rows, GSnake), color = (0, 255, 0)) #and generate a new treat! 
            
            
        for x in range(len(GSnake.body)): #if the snake hits itself
            
            if GSnake.body[x].position in list(map(lambda z:z.position, GSnake.body[x + 1:])): #formula for getting the snake parts and keeping them as a list for refrence.
                
                print("Total length: ", len(GSnake.body))
                
                Message_box("Game Over", "up for another round?")
                
                GSnake.reset((10, 10))
                
                break
                
        
        RedrawSquares(GBoard) #forces game to redraw after each movement
        
        
        
    
    


#game running starts here
if __name__ == '__main__':
    
    main()


