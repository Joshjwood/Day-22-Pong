from turtle import Turtle, Screen
from paddle import Paddle
from balls import Ball
from scoreboard import Score

import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle= Paddle((-350, 0))

ball = Ball()
scoreboard = Score()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True

timespeed = 0.10

while game_on:
    screen.update()
    time.sleep(timespeed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.flip()

    if ball.xcor() > 380:
        ball.flip()
        ball.reset()
        scoreboard.player1score()
        timespeed -= 0.01

    if ball.xcor() < -380:
        ball.flip()
        ball.reset()
        scoreboard.player2score()
        timespeed -= 0.01

    if timespeed == 0.01:
        game_on = False



screen.exitonclick()
