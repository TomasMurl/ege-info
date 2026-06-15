from turtle import *

k = 20
tracer(0)
screensize(4000, 4000)

rt(90)
for i in range(7):
    rt(45)
    fd(11 * k)
    rt(45)

up()
for x in range(-20, 10):
    for y in range(-10, 10):
        goto(x * k, y * k)
        dot(4)
done()