from turtle import *

k = 30
tracer(0)
screensize(4000, 4000)

lt(90)

for i in range(2):
    fd(28 * k)
    rt(90)
    fd(18 * k)
    rt(90)
up()
fd(14 * k)
rt(90)
fd(10 * k)
lt(90)
down()
for i in range(2):
    fd(30 * k)
    rt(90)
    fd(7 * k)
    rt(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(4)
done()