import turtle
import os
wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Space invader")
delay =input("press enter to finish")
border_pen=turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pensize(3)
