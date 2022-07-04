#this is a pong game wit ha turtle window!!

import turtle #creates a turtle window and allows configuration
import winsound #allows interaction with the windows sound library


Game_Window = turtle.Screen() #generates the standalone window in which we can play pong!

Game_Window.title("Pong created by Foxdarts") #titles the game window with developer name.

Game_Window.bgcolor("black") #sets the game window background(BG) to black

Game_Window.setup(width = 800, height = 600) #gives us a 800x600 pixel window to start with

Game_Window.tracer(0) #tracer lets us control the game speed using a manual update function.


#score tracking
Score_L = 0 #left score starts at 0

Score_R = 0 #right score starts at 0



#left paddle
paddle_L = turtle.Turtle() #generates the paddle within the turtle window

paddle_L.speed(0) #sets paddle speed to as fast as it can go

paddle_L.shape("square") #sets the "paddle" shape to a square

paddle_L.color("white") #sets teh paddle color to white

paddle_L.shapesize(stretch_wid = 5, stretch_len = 1) #streches the square up and down

paddle_L.penup() #stops thiss object from drawing a line as it moves

paddle_L.goto(-350, 0) #starts the paddle on the left side middle.


#right paddle
paddle_R = turtle.Turtle() #generates the paddle within the turtle window

paddle_R.speed(0) #sets paddle speed to as fast as it can go

paddle_R.shape("square") #sets the "paddle" shape to a square

paddle_R.color("white") #sets teh paddle color to white

paddle_R.shapesize(stretch_wid = 5, stretch_len = 1) #streches the square up and down

paddle_R.penup() #stops thiss object from drawing a line as it moves

paddle_R.goto(350, 0) #starts the paddle on the left side middle.


#ball!
ball = turtle.Turtle() #generates the Ball within the turtle window

ball.speed(0) #sets paddle speed to as fast as it can go

ball.shape("square") #sets the "paddle" shape to a square

ball.color("white") #sets teh paddle color to white

ball.penup() #stops thiss object from drawing a line as it moves

ball.goto(0, 0) #starts the paddle on the left side middle.

ball.dx = .2 #sets the speed of the ball on the x cord

ball.dy =.2 #sets speed of the ball on the y cord


#scoring pen
pen = turtle.Turtle() #creates a trutle for the object

pen.speed(0) #makes the animation speed infinite

pen.color("green") #sets the color to green

pen.penup() #makes it so there isnt a line drawn when the pen moves

pen.hideturtle() #hides the turtle. dont wanna see it untill it is used.

pen.goto(0, 260) #sets the score to upper right corner

pen.write("Player A: 0  Player B: 0", align = "center", font = ("Courier", 24, "normal"))


#movement functions
def paddle_L_UP():
    
    y = paddle_L.ycor() #gives us the y cord on the game board for the left paddle
    
    y += 20 #movees up 20 pixels
    
    paddle_L.sety(y) #sets the paddle 20 pizels up.
    
def paddle_L_Down():
    
    y = paddle_L.ycor() #gives us the y cord on the game board for the left paddle
    
    y -= 20 #movees down 20 pixels
    
    paddle_L.sety(y) #sets the paddle 20 pixels down.


def paddle_R_UP():
    
    y = paddle_R.ycor() #gives us the y cord on the game board for the left paddle
    
    y += 20 #movees up 20 pixels
    
    paddle_R.sety(y) #sets the paddle 20 pizels up.
    
def paddle_R_Down():
    
    y = paddle_R.ycor() #gives us the y cord on the game board for the left paddle
    
    y -= 20 #movees down 20 pixels
    
    paddle_R.sety(y) #sets the paddle 20 pixels down.

#left paddle movements
Game_Window.listen() #forces the game window to listen for keyboard input

Game_Window.onkeypress(paddle_L_UP, "w") #game listens for w key press and moves left paddle up.

Game_Window.onkeypress(paddle_L_Down, "s") #game listens for s key press and moves l paddle down.

#right paddle movement
Game_Window.onkeypress(paddle_R_UP, "Up") #game listens for o key press to move right paddle up

Game_Window.onkeypress(paddle_R_Down, "Down") #game listens for l key press to move right paddle down



#game loop starts here

while True: 
    
    Game_Window.update() #everytime the game loops this updates the window
    
    
    #ball movement
    ball.setx(ball.xcor() + ball.dx) #moves the ball on the x
    
    ball.sety(ball.ycor() + ball.dy) #moves the ball on the y
    
    
    
    #border set
    if ball.ycor() > 290: #if the ball hits the upper boarder
        
        ball.sety(290) #set the ball to the upper limit
        
        ball.dy *= -1 #and change its direction
        
        winsound.PlaySound('ting.wav' , winsound.SND_ASYNC) #adds a sound on border hit
        
    if ball.ycor() < -290: #if the ball hits the lower boarder
        
        ball.sety(-290) #set the ball to the lower limit
        
        ball.dy *= -1 #and change its direction
        
        winsound.PlaySound('ting.wav' , winsound.SND_ASYNC) #adds a sound on border hit
        
    if ball.xcor() > 390: #if the ball scores a point
        
        ball.goto(0, 0) #reset ball to 0
        
        ball.dx *= -1 #and starts ball heading the otherway.
        
        Score_L += 1 #adds a point to the left person
        
        pen.clear() #wipes the score board and allows to write each point
        
        pen.write(f"Player A: {Score_L}  Player B: {Score_R}", align = "center", font = ("Courier", 24, "normal")) #changes the score for the correct person each time a point is scored.

        
    if ball.xcor() < -390: #if the ball scores a point
        
        ball.goto(0, 0) #reset ball to 0
        
        ball.dx *= -1 #and starts ball heading the otherway.
        
        Score_R += 1 #adds ascore to the right person
        
        pen.clear() #wipes the score board and allows to write each point
        
        pen.write(f"Player A: {Score_L}  Player B: {Score_R}", align = "center", font = ("Courier", 24, "normal")) #changes the score for the correst person each time a point is scored.

    
    
    #paddle collision logic
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_R.ycor() + 40 and ball.ycor() > paddle_R.ycor() - 40): #if the ball hits the paddle area and isnt behind the paddle
        
        ball.setx(340) #sets the ball a little bit more center
        
        ball.dx *= -1 #and changes direction
        
        winsound.PlaySound('Paddle.wav', winsound.SND_ASYNC) #adds a sound on paddle hit.
    
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_L.ycor() + 40 and ball.ycor() > paddle_L.ycor() - 40): #if the ball hits the paddle area and isnt behind the paddle
        
        ball.setx(-340) #sets the ball a little bit more center
        
        ball.dx *= -1 #and changes direction
        
        winsound.PlaySound('Paddle.wav', winsound.SND_ASYNC) #adds a sound on paddle hit.
    