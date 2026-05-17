from turtle import *

k = 20
tracer(0)
screensize(4000, 4000)

for i in range(3):
    fd(7 * k)
    rt(90)
    fd(12 * k)
    rt(90)
up()
fd(4 * k)
rt(90)
fd(6 * k)
lt(90)
down()
for i in range(4):
    fd(83 * k)
    rt(90)
    fd(77 * k)
    rt(90)

up()
for x in range(-100, 10):
    for y in range(-15, 100):
        goto(x * k, y * k)
        dot(4)
done()