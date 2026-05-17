from turtle import *

k = 100
tracer(0)
screensize(4000, 4000)
for i in range(7):
    fd(10 * k)
    rt(120)
up()
for x in range(-10, 20):
    for y in range(-10, 10):
        goto(x * k, y * k)
        dot(4)
done()
