from turtle import *

k = 80
tracer(0)
screensize(4000, 4000)

rt(30)
for i in range(3):
    rt(150)
    fd(6 * k)
    rt(30)
    fd(12 * k)

up()
for x in range(-20, 10):
    for y in range(-10, 10):
        goto(x * k, y * k)
        dot(4)
done()