from turtle import *

k = 70
tracer(0)
screensize(2000, 2000)

lt(90)

rt(90)
for i in range(3):
    rt(45)
    fd(10 * k)
    rt(45)
rt(315)
fd(10 * k)
for i in range(2):
    rt(90)
    fd(10 * k)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * k, y * k)
        dot(4)
done()