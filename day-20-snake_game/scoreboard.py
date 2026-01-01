from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        #self.high_score = 0
        self.high_score = self.get_high_score()
        self.penup()
        self.goto(0, 250)
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.set_high_score()

        self.score = 0
        self.update_scoreboard()

    def get_high_score(self):
        with open("data.txt") as file:
            high_sore = file.read()

        return int(high_sore)

    def set_high_score(self):
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))

    # def game_over(self):
    #     self.goto(0, 0)
    #     # self.write(f"Game Over", move=False, align=ALIGNMENT, font=FONT)
