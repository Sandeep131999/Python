from turtle import Turtle, Screen
import random

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    ran_color = (r,g,b)
    return ran_color

screen = Screen()
screen.colormode(255)

t = Turtle()
t.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        t.circle(100)
        t.color(random_color())
        t.setheading(t.heading()+size_of_gap)

draw_spirograph(5)

screen.exitonclick()



