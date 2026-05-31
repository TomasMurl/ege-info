from turtle import *

k = 30
tracer(0)
screensize(4000, 4000)

rt(90)
for i in range(7):
    fd(11 * k)
    rt(45)
    fd(8 * k)
    rt(135)

up()
for x in range(-10, 50):
    for y in range(-40, 40):
        goto(x * k, y * k)
        dot(4)
done()