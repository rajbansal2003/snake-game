from turtle import Turtle
ALLIGNMENT = "center"
FONT = ("Arial", 15, "normal")
class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        # self.update_score()
        self.hideturtle()

    def update_score(self):
        # turtle.write function is used to write on the screen, parameters -> a string to write, align = where you want to place, font = accepts in tuple eg ("type", size, "style")
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.high_score}", align=ALLIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
            # Now this will not lose the high score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            # Now this will not lose the high score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.penup()
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALLIGNMENT, font=FONT)