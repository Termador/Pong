#pong in python 3 terminal w/ turtle !

import turtle
import random 

window = turtle.Screen()
window.title(" Pong ! ")
window.setup(width = 800, height = 600)
window.bgcolor("black")
window.tracer(0)

random_color_list = ["red", "white", "green", "blue", "yellow", "purple"]
player1_counter = 0
player2_counter = 0 

def create_paddle(paddle_name, speed, shape, color, location_X, location_Y, length, width):
    paddle_name = turtle.Turtle()
    paddle_name.speed(speed)
    paddle_name.shape(shape)
    paddle_name.color(color)
    paddle_name.penup()
    paddle_name.goto(location_X, location_Y)
    paddle_name.turtlesize(length,width)
    return paddle_name

def create_ball():
    ball = turtle.Turtle()
    ball.penup()
    ball.speed(0)
    ball.shape("circle")
    ball.color("red")
    ball.goto(0,0)
    ball.dx = 0.3
    ball.dy = 0.3
    return ball

def create_player(player_number, location_X, location_Y, Text = str):
    player_number = turtle.Turtle()
    player_number.hideturtle()
    player_number.color("white")
    player_number.penup()
    player_number.goto(location_X, location_Y)
    player_number.write(Text)
    return player_number

paddle1 = create_paddle("paddle1", 0, "square", "blue", -350, 0, 5, 1/2)
paddle2 = create_paddle("paddle2", 0, "square", "purple", 350, 0, 5, 1/2)
ball = create_ball()
player1 = create_player("player1", -200, 275, "Player 1: 0")
player2 = create_player("player2", 200, 275, "Player 2: 0")

def paddle1_up():
    y = paddle1.ycor()
    y += 20
    paddle1.sety(min(y, 280))
   
def paddle1_down():
    y = paddle1.ycor()
    y -= 20
    paddle1.sety(max(y, -280))

def paddle2_up():
    y = paddle2.ycor()
    y += 20
    paddle2.sety(min(y,280))

def paddle2_down():
    y = paddle2.ycor()
    y -= 20
    paddle2.sety(max(y,-280))

window.listen()
window.onkeypress(paddle1_up, "w")
window.onkeypress(paddle1_down, "s")
window.onkeypress(paddle2_up, "i")
window.onkeypress(paddle2_down, "k")

while True:
    window.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 
    
    if ball.ycor() >= (paddle1.ycor() - 50) and ball.ycor() <= (paddle1.ycor() + 50):
        if ball.xcor() >= (paddle1.xcor()) and ball.xcor() <= paddle1.xcor() + 5 :
            ball.dx *= -1
    if ball.ycor() >= (paddle2.ycor() - 50) and ball.ycor() <= (paddle2.ycor() + 50):
        if ball.xcor() >= (paddle2.xcor() - 5) and ball.xcor() <= (paddle2.xcor()):
            ball.dx *= -1

    if ball.xcor() > 400:
        player1_counter += 1
        player1.clear()
        written_text1 = "Player1: " + str(player1_counter)
        player1.write(written_text1)
        ball.color(random.choice(random_color_list))
        ball.goto(0,0)
        ball.dx *= -1
        
    if ball.xcor() < -400: 
        player2_counter += 1
        player2.clear()
        written_text2 = "Player2: " + str(player2_counter)
        player2.write(written_text2)
        ball.color(random.choice(random_color_list))
        ball.goto(0,0)
        ball.dx *= -1
        
