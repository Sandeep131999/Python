from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_paddle_score = 0
        self.r_paddle_score = 0
        self.update_score_board()

    def update_score_board(self):
        self.goto(-100,250)
        self.common_print(self.l_paddle_score)
        self.goto(100, 250)
        self.common_print(self.r_paddle_score)

    def common_print(self,score):
        self.write(f"score : {score}",
                   align="center", font=("Arial", 20, "normal"))

    def increase_l_score(self):
        self.clear()
        self.l_paddle_score +=1
        self.update_score_board()

    def increase_r_score(self):
        self.clear()
        self.r_paddle_score +=1
        self.update_score_board()