from turtle import *
from random import randint
bgcolor("pink")
x=1
speed(0)
while x < 300:
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    colormode(255)
    pencolor(r,g,b)
    fd(40+x)
    rt(250.990)
    x = x+1
exitonclick()


