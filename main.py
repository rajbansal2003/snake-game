from turtle import Screen
from snake import Snake
from food import Food
from scorecard import Scorecard
import time

screen = Screen()

# set the screen for the snake game
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # turn ON/OFF-screen animation

snake = Snake()
food = Food()
scorecard = Scorecard()

# control the snake movement with keyboard
screen.listen()
# by using Arrow keys
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
# by using w, a, s, d keys
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True
speed = 1
while game_is_on:
    screen.update()  # update turtle screen
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15: # detect function detects the distance b/w 2 objects of turtle
        food.refresh()
        snake.extend()
        scorecard.increase_score()


    # detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scorecard.reset()
        # scorecard.game_over()
        a = 5
        # when lost, then just show small animation by changing the background color 5 times
        while a > 0:
            screen.bgcolor("white")
            time.sleep(0.1)
            screen.bgcolor("black")
            time.sleep(0.1)
            a -= 1
        snake.reset()

    # detect collision with tail & any other part

    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         game_is_on = False
    #         scorecard.game_over()
    for segment in snake.segments[1:]:
        # here we use the concept of slicing, we can not consider the head while collision
        if snake.head.distance(segment) < 10:
            scorecard.reset()
            # scorecard.game_over()
            a = 5
            while a>0:
                screen.bgcolor("white")
                time.sleep(0.1)
                screen.bgcolor("black")
                time.sleep(0.1)
                a -= 1
            snake.reset()

screen.exitonclick()