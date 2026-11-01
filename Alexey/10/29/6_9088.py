from turtle import *
k = 20
tracer(0)
screensize(4000, 4000)

for i in range(5):
    fd(33 * k)
    rt(135)
    fd(33 * k)
    rt(45)

up()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * k, y * k)
        dot(4)
done()