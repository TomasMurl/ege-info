from turtle import *

k = 20
tracer(0)
screensize(4000, 4000)
left(90)

rt(45)
for i in range(2):
    fd(24 * k)
    rt(90)
    fd(10 * k)
    rt(90)
fd(5 * k)
lt(90)
fd(12 * k)
rt(90)
for i in range(2):
    fd(9 * k)
    rt(90)
    fd(35 * k)
    rt(90)

up()
for x in range(-10, 40):
    for y in range(-30, 40):
        goto(x * k, y * k)
        dot(4)
done()