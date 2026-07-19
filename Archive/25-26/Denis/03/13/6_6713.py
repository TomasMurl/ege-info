from turtle import *

k = 20
screensize(4000, 4000)
tracer(0)
left(90)

for i in range(2):
    forward(13 * k)
    right(90)
    forward(20 * k)
    right(90)
up()
forward(8 * k)
right(90)
backward(3 * k)
left(90)
down()
for i in range(2):
    forward(16 * k)
    right(90)
    forward(8 * k)
    right(90)

up()
for x in range(-20, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(4)
done()