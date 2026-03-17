from turtle import *

k = 20
tracer(0)
screensize(4000, 4000)

left(90)

for i in range(8):
    fd(22 * k)
    rt(90)
    fd(33 * k)
    rt(90)
up()
bk(8 * k)
rt(90)
fd(11 * k)
lt(90)
down()
for i in range(8):
    fd(73 * k)
    rt(90)
    fd(62 * k)
    rt(90)

up()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * k, y * k)
        dot(4)
done()

print(11 * 22 + 73 * 62)
# 4768