from turtle import *

k = 20
tracer(0)
screensize(2000, 2000)
lt(90)

rt(90)
for i in range(7):
    fd(11 * k)
    rt(45)
    fd(8 * k)
    rt(135)

up()
for x in range(-10, 20):
    for y in range(-10, 10):
        goto(x * k, y * k)
        dot(4)
done()