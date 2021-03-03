from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.write(f"Level: {self.level}", align= "left", font= FONT)

    def increase_lev(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="left", font=FONT)
    def over(self):
        self.penup()
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", align="center", font=("Courier", 24, "bold"))
