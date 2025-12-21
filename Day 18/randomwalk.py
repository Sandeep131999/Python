from turtle import Turtle,Screen
import random

def create_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# --- Screen must be created first ---
screen = Screen()
screen.colormode(255)

# --- Then create the turtle ---
t = Turtle()
t.pensize(7)

directions = [0,90,180,270]

for _ in range(0,100):
    t.color(create_random_color())
    t.forward(30)
    t.setheading(random.choice(directions))

screen.exitonclick()