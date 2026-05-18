from turtle import *

k = 20
tracer(0)
screensize(4000, 4000)

for i in range(2):
    fd(1 * k)
    lt(270)
    fd(16 * k)
    rt(90)
up()
bk(4 * k)
rt(90)
fd(10 * k)
lt(90)
down()
for i in range(2):
    fd(17 * k)
    rt(90)
    fd(7 * k)
    rt(90)

up()
for x in range(-10, 20):
    for y in range(-30, 10):
        goto(x * k, y * k)
        dot(4)
done()

print(7 * 17 + 10)