from turtle import  Turtle

class ScoreBoard(Turtle) :

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280,250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level :{self.level}", False, "left", ("Arial", 15, "normal"))

    def increase_level(self):
        self.level += 1

    def game_over (self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "left", ("Arial", 15, "normal"))