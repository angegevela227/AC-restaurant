# Python program to draw square
# using Turtle Programming
import turtle
skk = turtle.Turtle()
skk.pensize(4)

for i in range(4):
    skk.forward(100)
    skk.color('grey')
    skk.right(90)
    skk.color('maroon')
    skk.forward(100)
    skk.color('white')
    skk.right(90)
    skk.color('grey')
    skk.forward(100)
    skk.left(90)
turtle.done()