import turtle
turtle.title("Draw")
def up():
  turtle.forward(5)
def down():
  turtle.backward(5)
def right():
  turtle.left(10)
def left():
  turtle.right(10)
turtle.showturtle()
turtle.left(90)
turtle.onkey(up, "Up")
turtle.onkey(down, "Down")
turtle.onkey(right, "Right")
turtle.onkey(left, "Left")
turtle.listen()
print("Use Arrow Keys To Move")
