from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True

while game_is_on:

    screen.update()
    ball.move()
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Detectar la colision con la paleta derecha
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50and ball.xcor() < -320:
        ball.bounce_x()

    # Detectar cuando la paleta derecha le erra
    if ball.xcor() > 380 :
        ball.reset_poistion()
        scoreboard.l_point()

    # Detectar cuando la paleta derecha le erra
    if ball.xcor() < -380:
        ball.reset_poistion()
        scoreboard.r_point()


screen.exitonclick()
