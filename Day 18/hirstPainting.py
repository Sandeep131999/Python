import random
import colorgram
from turtle import  Turtle,Screen
rgb_colors = [(252, 249, 244), (53, 100, 157), (12, 36, 74), (242, 159, 177), (191, 132, 217), (246, 177, 206), (109, 195, 187), (154, 196, 217), (237, 144, 76), (202, 76, 4), (224, 167, 167), (220, 0, 0), (61, 182, 177)]
# colors = colorgram.extract('chose_colors.png', 13)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

screen = Screen()
screen.colormode(255)

t = Turtle()
t.speed("fastest")
t.penup()
t.hideturtle()
t.setheading(225)
t.forward(300)
t.setheading(0)
number_of_dots = 100

for dot_count in range(1,number_of_dots +1):
    t.dot(20, random.choice(rgb_colors))
    t.forward(50)

    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)



screen.exitonclick()