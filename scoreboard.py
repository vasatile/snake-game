from turtle import Turtle

ALIGNMET = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
           self.high_score = int(data.read())
        self.color("black")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"score : {self.score} High Score: {self.high_score}", align=ALIGNMET, font=FONT)





    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.update_scoreboard()







    def game_master(self):
        self.goto(0, 0)
        self.write(f"GAME MASTER", align=ALIGNMET, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
