from turtle import *

k = 20
tracer(0)
screensize(4000, 4000)

for i in range(2):
    fd(13 * k)
    rt(90)
    fd(20 * k)
    rt(90)
up()
fd(8 * k)
rt(90)
backward(3 * k)
lt(90)
down()
for i in range(2):
    fd(16 * k)
    rt(90)
    fd(8 * k)
    rt(90)

up()
for x in range(-10, 30):
    for y in range(-30, 10):
        goto(x* k, y*k)
        dot(4)
done()