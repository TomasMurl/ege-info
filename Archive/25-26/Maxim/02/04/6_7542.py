from turtle import *

tracer(0)
screensize(4000, 4000)
k = 20
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
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(4)
done()