#Building a turtle race
from turtle import Turtle,Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput("make your bet","which turtle win the race ? enter a color :")
colors = ["red","orange","yellow","green","blue","purple"]
y_positions = [-140,-100,-60,-20,20,60]
all_turtles = []

for index in range(6):
    new_turtle= Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(-185,y_positions[index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>200:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you have won the {winning_color}turtle is the winner")
            else:
                print(f"you have lost the game {winning_color} turtle is the winner")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()