import colorgram
from turtle import Turtle, Screen
import random

# list_of_colors = colorgram.extract('image.jpg', 30)
# list_of_rgb = []
#
# for color in list_of_colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#
#     rgb_tuple = (r, g, b)
#     list_of_rgb.append(rgb_tuple)
# print(list_of_rgb)

color_list = [(206, 161, 82), (55, 88, 129), (142, 91, 41), (221, 207, 107), (138, 26, 48), (133, 175, 200),
              (157, 47, 84), (46, 55, 102), (169, 159, 41), (131, 188, 145), (82, 20, 43), (36, 43, 68),
              (186, 93, 106), (189, 139, 163), (87, 115, 177), (87, 156, 97), (59, 39, 33), (79, 154, 165),
              (196, 81, 71), (54, 128, 122), (45, 73, 76), (162, 202, 216), (44, 75, 73), (78, 76, 45),
              (167, 207, 165), (219, 175, 187)]

screen = Screen()
screen.colormode(255)

manuelita = Turtle()
manuelita.penup()
manuelita.hideturtle()

x_offset = -200
y_offset = 200
manuelita.setposition(x_offset, y_offset)
manuelita.speed(100)


def draw_dot(one_color):
    manuelita.dot(20, one_color)
    manuelita.penup()
    manuelita.forward(50)


for row in range(10):
    for column in range(10):
        color = random.choice(color_list)
        draw_dot(color)
    y_offset += -50
    manuelita.setposition(x_offset, y_offset)

screen.exitonclick()
