import turtle
import winsound 


wn=turtle.Screen()
wn.title("painful pong and not finished yet")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#paddy
paddy_a=turtle.Turtle()
paddy_a.speed(0)
paddy_a.shape("square")
paddy_a.color("white")
paddy_a.shapesize(stretch_wid=5,stretch_len=1)
paddy_a.penup()
paddy_a.goto(-350,0)

paddy_b=turtle.Turtle()
paddy_b.speed(0)
paddy_b.shape("square")
paddy_b.color("white")
paddy_b.shapesize(stretch_wid=5,stretch_len=1)
paddy_b.penup()
paddy_b.goto(350,0)

#balls
ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=1.4
ball.dy=1.4

#fungsion
def paddy_a_up():
    y=paddy_a.ycor()
    y+=50
    paddy_a.sety(y)

def paddy_a_down():
    y=paddy_a.ycor()
    y-=50
    paddy_a.sety(y)
    
def paddy_b_up():
    y=paddy_b.ycor()
    y+=50
    paddy_b.sety(y)

def paddy_b_down():
    y=paddy_b.ycor()
    y-=50
    paddy_b.sety(y)
    
#keybind
wn.listen()
wn.onkeypress(paddy_a_up,"w")
wn.onkeypress(paddy_a_down,"s")
wn.onkeypress(paddy_b_down,"l")
wn.onkeypress(paddy_b_up,"o")

#game loop
while True:
    wn.update()
    
    #ballsmove
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    
    #border
    if ball.ycor()> 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("beep.wav",winsound.SND_ASYNC)
        
    if ball.ycor()< -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("beep.wav",winsound.SND_ASYNC)
        
    if ball.xcor()> 400:
        ball.setx(400)
        ball.dx *= -1
    
    if ball.xcor()<-400:
        ball.setx(-400)
        ball.dx *= -1
        
    #bonk
    if ball.xcor()>340 and (ball.ycor()<paddy_b.ycor()+50 and ball.ycor()>paddy_b.ycor()  -50):
        ball.dx *= -1
    
    if ball.xcor()<-340 and (ball.ycor()<paddy_a.ycor()+50 and ball.ycor()>paddy_a.ycor()  -50):
        ball.dx *= -1
