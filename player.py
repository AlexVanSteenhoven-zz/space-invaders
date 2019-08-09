import turtle as t


class Player:
    # Create the player
    player = t.Turtle()
    player.color('blue')
    player.shape('triangle')
    player.penup()
    player.speed(0)
    player.setposition(0, -250)
    player.setheading(90)
