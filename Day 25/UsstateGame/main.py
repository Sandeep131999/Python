import turtle
import pandas
from pandas.io.formats.format import return_docstring

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
guessed_states = []
while len(data) <= 50 :
    answer_state = screen.textinput(f"Guess the State {len(guessed_states)}/{(len(data))}",
                                    "Whats another state's name").title()
    state_row = data[data["state"] == answer_state]
    if not state_row.empty:
        x = int(state_row["x"].values[0])
        y = int(state_row["y"].values[0])
        turtle.tracer(0)
        guessed_states.append(state_row)
        missing_states = [state for state in list(data)]
        print(missing_states)
        turtle.penup()
        turtle.goto(x,y)
        turtle.write(state_row["state"].values[0], align="center",font=("Arial", 12, "normal"))

        turtle.goto(0,0)


# turtle.mainloop()

