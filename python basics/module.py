import turtle

myshape = turtle.Turtle()

screen = turtle.Screen()
screen.bgcolor("gray")

myshape.shape("turtle")
myshape.color("green")

distance = 50
for i in range(10):
    myshape.forward(distance)
    myshape.right(90)
    distance = distance + 10

turtle.done()