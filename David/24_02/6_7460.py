from turtle import *

k = 30
tracer(0)
screensize(4000,4000)

for i in range(9):
    forward(22*k)
    right(90)
    forward(6*k)
    right(90)

up()
forward(1*k)
right(90)
forward(5*k)
left(90)
down()

for i in range(9):
    forward(53*k)
    right(90)
    forward(75*k)
    right(90)
up()
for x in range(-10, 30):
    for y in range(-10, 10):
        goto(x * k, y * k)
        dot(4)
done()