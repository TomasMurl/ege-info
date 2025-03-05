from turtle import *

left(90)
k = 80
screensize(4000, 4000)
tracer(0)

for i in range(2):
    fd(6 * k)
    rt(90)
    fd(4 * k)
    rt(90)
up()
fd(2 * k)
rt(90)
bk(4 * k)
lt(90)
down()
for i in range(2):
    fd(5 * k)
    rt(90)
    fd(7 * k)
    rt(90)
up()

for x in range(-6, 5):
    for y in range(0, 8):
        goto(x * k, y * k)
        dot(8)

done()
