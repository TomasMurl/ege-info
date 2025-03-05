from turtle import *

tracer(0)
screensize(2000, 2000)
k = 20
left(90)

for i in range(2):
    fd(16 * k)
    right(90)
    fd(9 * k)
    rt(90)
up()
fd(5 * k)
right(90)
fd(11 * k)
rt(90)
down()
for i in range(2):
    fd(20 * k)
    right(90)
    fd(8 * k)
    rt(90)
up()

for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * k, y * k)
        dot(5)
done()