from turtle import *
k = 20
tracer(0)
screensize(4000, 4000)

for i in range(6):
    fd(24 * k)
    rt(90)
    fd(30 * k)
    rt(90)
up()
fd(2 * k)
rt(90)
fd(10 * k)
lt(90)
down()
for i in range(6):
    fd(75 * k)
    rt(90)
    fd(71 * k)
    rt(90)

up()
for x in range(-20, 100):
    for y in range(-100, 20):
        goto(x * k, y * k)
        dot(4)
done()
