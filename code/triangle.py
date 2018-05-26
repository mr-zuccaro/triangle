#!/usr/bin/python

import turtle #import the turtle library functions

turtle.shape("turtle")
turtle.shapesize(5, 5, 5)
turtle.speed(3)
turtle.color("green")

side1 = 222 #length of side of triangle

# green triangle
turtle.penup()
turtle.setpos(-200,150)
turtle.pensize(7)
turtle.pendown()

for i in range(3):
	turtle.forward(side1)
	turtle.right(120)	

turtle.done()
