from turtle import Turtle
import random as r

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        # this shapesize function resize the shape, 0.5 means the half of actual
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = r.randint(-280, 280)
        random_y = r.randint(-280, 280)
        self.goto(random_x, random_y)