from turtle import *

tracer(0) 
screensize(2000, 2000)
k = 20
left(90)

for _ in range(2):
    fd(6 * k)
    rt(90)
    fd(12*k)
    rt(90)
up()
fd(1 * k)
rt(90)
fd(3 * k)
lt(90)
down()
for _ in range(2):
    fd(77 * k)
    rt(90)
    fd(45 * k)
    rt(90)

up()
for x in range(-10, 30):
    for y in range(-10, 10):
        goto(x * k, y * k)
        dot(4)
done()
