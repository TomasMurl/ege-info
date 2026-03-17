from turtle import *

k = 20
screensize(4000, 4000)
tracer(0)
left(90)

for i in range(6):
    forward(33 * k)
    right(90)
    forward(20 * k)
    right(90)
up()
forward(3 * k)
right(90)
forward(9 * k)
left(90)
down()
for i in range(6):
    forward(24 * k)
    right(90)
    forward(25 * k)
    right(90)

up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(4)
done()