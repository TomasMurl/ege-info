from turtle import *
tracer(0)
screensize(4000,4000)
k = 10


for i in range(2):
    forward(21*k)
    right(90)
    forward(27 * k)
    right(90)
up()
fd(9*k)
right(90)
fd(10*k)
left(90)
down()
for i in range(2):
    forward(86*k)
    right(90)
    forward(47 * k)
    right(90)

up()
for x in range(-10,100):
    for y in range(-100,20):
        goto(x*k,y*k)
        dot(4)
done()