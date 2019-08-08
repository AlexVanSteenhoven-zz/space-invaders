import turtle as t
import os


class Screen:
    # Setup the Screen
    win = t.Screen()
    win.bgcolor('black')
    win.title('Space Invaders')

    # Draw a border
    # bp = border pen
    bp = t.Turtle()
    bp.speed(0)
    bp.color('white')
    bp.penup()
    bp.setposition(-300, -300)
    bp.pendown()
    bp.pensize(3)

    # draw square (border)
    # s = side
    for s in range(4):
        bp.fd(600)
        bp.lt(90)
    bp.hideturtle()

    delay = input('Press enter to quit')
