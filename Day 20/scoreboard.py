from importlib.metadata import files
from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        with open("score.txt", "r") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"score: {self.score} High score {self.high_score}", False, "center", ("Arial", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset_score(self):

        if self.score > self.high_score :
            self.high_score = self.score
            with open("score.txt", "w") as file:
                file.write(str(self.score))
            self.score = 0
            self.clear()
            self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", False, "center", ("Arial", 20, "normal"))
