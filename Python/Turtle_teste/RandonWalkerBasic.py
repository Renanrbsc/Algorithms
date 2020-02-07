import turtle
from random import randint

t1 = turtle.Turtle()
t1.speed(0)

while True:
  t1.forward(5)
  t1.right(randint(-45,45))
