#ping pong game
#create the screen
#create a move paddle
#create another paddle
#create the ball and make it move
#detect collision with wall bounce
#Detect the collision with paddle
#Detect when paddle misses
#keep score

from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import  ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score_board = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on :
    time.sleep(0.2)
    ball.move()
    screen.update()


    #Detect collision with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()


    #Detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # #Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score_board.increase_l_score()

    if ball.xcor() < -380:
        ball.reset_position()
        score_board.increase_r_score()


screen.exitonclick()