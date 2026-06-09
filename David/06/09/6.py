from turtle import *

k = 20
tracer(0)
screensize(4000, 4000)

for i in range(2):
    fd(14 * k)
    rt(90)
    fd(18 * k)
    rt(90)
up()
fd(3 * k)
rt(90)
fd(7 * k)
lt(90)
down()
for i in range(2):
    fd(74 * k)
    rt(90)
    fd(92 * k)
    rt(90)

up()
for x in range(-10, 100):
    for y in range(-100, 10):
        goto(x * k, y * k)
        dot(4)
done()