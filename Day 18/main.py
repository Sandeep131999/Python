from turtle import Turtle,Screen
import random

# def draw_shapes(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         t.forward(100)
#         t.right(angle)
#
# for shape_side_n in range(3,11):
#     draw_shapes(shape_side_n

def create_random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_colors = (r,g,b)
    return random_colors

#Randow walk
# 0 -> East ,90->north ,180->west,270-
t = Turtle()
for _ in range(100):
    directions=[0,90,180,270]
    t.pensize(7)
    t.forward(30)
    t.setheading(random.choice(directions))



