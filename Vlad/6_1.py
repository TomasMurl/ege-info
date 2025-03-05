from turtle import *

# up()
# down()
# forward(x) , fd(x)
# backward(x) , bk(x)
# right(a) , rt(a)
# left(a) , lt(a)

# goto(x, y) - переместиться в точку
# dot(x) - поставить точку (x - толщина точки)

# screensize(4000, 4000)
# tracer(0)
# done()
screensize(4000, 4000)
tracer(0)
left(90)
k = 60
for i in range(2):
    fd(5 * k)
    rt(90)
    fd(7 * k)
    rt(90)
up()
bk(2 * k)
rt(90)
fd(3 * k)
lt(90)
down()
for i in range(2):
    fd(4 * k)
    rt(90)
    fd(6 * k)
    rt(90)
up()

for x in range(-10, 10):
    for y in range(-10, 10):
        goto(x * k, y * k)
        dot(5)
done()