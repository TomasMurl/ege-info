from turtle import *

k = 30
tracer(3)
screensize(8000, 8000)

for i in range(3):
    fd(14 * k)
    lt(270)
    bk(18 * k)
    rt(90)
up()
fd(4 * k)
rt(90)
bk(16 * k)
lt(90)
down()
for i in range(4):
    fd(18 * k)
    rt(270)
    fd(20 * k)
    rt(270)

up()
for x in range(-10, 20):
    for y in range(-20, 20):
        goto(x * k, y * k)
        dot(4)
done()