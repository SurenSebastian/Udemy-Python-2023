import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a Color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y_position = [-70, -40, -10, 20, 50, 80]
all_turtules = []

for turtel_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtel_index])
    new_turtle.goto(x=-230, y=y_position[turtel_index])
    all_turtules.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtules:
        if turtle.xcor()> 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
# angle = 10
# step = 10
#
# def move_forwards():
#     manu.forward(step)
#
# def move_backwards():
#     manu.backward(step)
#
# def turn_counter_clockwise():
#     manu.left(angle)
#
#
# def turn_clockwise():
#     manu.right(angle)
#
#
# def clear_drawing():
#     manu.reset()
#
# def pen_down():
#     manu.pendown()
#
#
# def pen_up():
#     manu.penup()
#
#
# screen.listen()
# screen.onkey(key = "w", fun = move_forwards)
# screen.onkey(key = "s", fun = move_backwards)
# screen.onkey(key = "a", fun = turn_counter_clockwise)
# screen.onkey(key = "d", fun = turn_clockwise)
# screen.onkey(key = "c", fun = clear_drawing)
# screen.onkey(key = "p", fun = pen_down)
# screen.onkey(key = "u", fun = pen_up)
# screen.exitonclick()