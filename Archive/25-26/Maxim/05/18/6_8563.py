from turtle import *

k = 20
tracer(0)
screensize(4000, 4000)

for i in range(6):
    fd(33 * k)
    rt(90)
    fd(20 * k)
    rt(90)
up()
fd(3 * k)
rt(90)
fd(9 * k)
lt(90)
down()
for i in range(6):
    fd(24 * k)
    rt(90)
    fd(25 * k)
    rt(90)

up()
for x in range(-10, 50):
    for y in range(-50, 10):
        goto(x * k, y * k)
        dot(4)
done()