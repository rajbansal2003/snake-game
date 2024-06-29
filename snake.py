from turtle import Turtle
from scorecard import Scorecard
import time

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
# moving angles
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

scorecard = Scorecard()
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.speed = 0

    def create_snake(self):
        # when game starts, 3 segment of snake automatically becomes
        for position in STARTING_POSITION:
            self.add_segment(position)
        time.sleep(1)

    def add_segment(self, position):
        timmy = Turtle(shape="square")
        timmy.color("white")
        timmy.penup()
        timmy.goto(position)
        self.segments.append(timmy)

    def reset(self):
        # when it is called, all the turtle created destroy & game start again from starting
        for seg in self.segments:
            # this loop added bcz when we lost, then this sends the snake out of the screen
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        # as the snake hit the food, it adds the segment into the snake
        self.add_segment(self.segments[-1].position())
    def move(self):
        # for seg_num in range(start= 2, stop= 0, step= -1): # example 2, 1, 0 ........
        # this range function can be run as we set value above, from start to end with required number of step size but if we write keyword here then get error
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # self.segments[seg_num].speed(self.speed)
            # if scorecard.score%10 == 0:
            #     self.speed += 1
            # this code will make the snake body to follow the first square
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    """
                     | (up = 90)
     (left = 180) <- . -> (right = 0)
                     | (down = 270)
    """

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
