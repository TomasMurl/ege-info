from turtle import *

k = 50
tracer(0)
screensize(4000, 4000)
lt(90)

for i in range(2):
    fd(6 * k)
    rt(90)
    fd(12 * k)
    rt(90)
up()
fd(1 * k)
rt(90)
fd(3 * k)
lt(90)
down()
for i in range(2):
    fd(77 * k)
    rt(90)
    fd(45 * k)
    rt(90)

up()
for x in range(-10, 20):
    for y in range(-10, 10):
        goto(x * k, y * k)
        dot(4)
done()