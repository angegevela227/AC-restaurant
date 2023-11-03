import turtle
#making the turtle
t = turtle.Turtle()
#commands
t.forward(10)
t.colour('green')
t.left(90)
t.penup()
t.goto(0,0)
t.pendown()
for i in range(45): #circle
  t.forward(1)
  t.right(8)
for i in range(3): #Triangle
  t.forward(10)
  t.left(135)