from turtle import *

k = 20
tracer(0)
screensize(4000, 4000)
left(90)

for i in range(8):
    fd(22 * k)
    right(90)
    fd(33 * k)
    right(90)
up()
backward(8 * k)
rt(90)
fd(11 * k)
lt(90)
down()
for i in range(8):
    fd(73 * k)
    right(90)
    fd(62 * k)
    right(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(4)
done()