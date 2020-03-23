import turtle
import os
import pygame

window = turtle.Screen()
window.title("Pong by Trevor Drayton")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0) #Stops the window from updating, so we have to manually update the game (do this for speed)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #speed of animation (sets to max possible speed)
paddle_a.shape("square") #built in shape
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) #stretched y coordinate of paddle by 5 as a scalar
paddle_a.penup() #turtles by definition draw a line as they're moving. this stops that from happening
paddle_a.goto(-350, 0) #coordinates


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #speed of animation (sets to max possible speed)
paddle_b.shape("square") #built in shape
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) #stretched y coordinate of paddle by 5 as a scalar
paddle_b.penup() #turtles by definition draw a line as they're moving. this stops that from happening
paddle_b.goto(350, 0) #coordinates

# Ball
ball = turtle.Turtle()
ball.speed(0) #speed of animation (sets to max possible speed)
ball.shape("square") #built in shape
ball.color("white")
ball.penup() #turtles by definition draw a line as they're moving. this stops that from happening
ball.goto(0, 0) #coordinates
ball.dx = .25 #every time the ball moves, it moves by .4 pixels right (depends on computer speed)
ball.dy = .25 #every time the ball moves, it moves by .4 pixels up (depends on computer speed)

# PEN
pen = turtle.Turtle()
pen.speed(0)
pen.color("White")
pen.penup() #turtles by definition draw a line as they're moving. this stops that from happening
pen.hideturtle() #dont want to see pen, just text it'll write
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))

# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard binding
window.listen() #listen for input
window.onkeypress(paddle_a_up, "w") #when the user presses w, call the function paddle_a_up
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

# Music
pygame.mixer.init()
pygame.mixer.music.load("YouGonLearn.mp3")
pygame.mixer.music.play(-1,0.0)

# Main game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear() #clears the score (happens so fast you don't see it)
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear() #clears the score (happens so fast you don't see it)
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40) and ball.ycor() > paddle_b.ycor() -40:
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() < -350) and (ball.ycor() < paddle_b.ycor() + 40) and ball.ycor() > paddle_a.ycor() -40:
        ball.setx(-340)
        ball.dx *= -1