from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_left():
    tim.setheading(tim.heading()+10)

def move_right():
    tim.setheading(tim.heading()-10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()

screen.listen()
screen.onkey(move_forward,"w")
screen.onkey(move_backward,"s")
screen.onkey(move_left,"l")
screen.onkey(move_right,"r")
screen.onkey(clear_screen,"space")


screen.exitonclick()