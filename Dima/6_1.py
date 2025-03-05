from turtle import *

tracer(0)
screensize(2000, 2000)
k = 20
lt(90)

for i in range(2):
    fd(16 * k)
    rt(90)
    fd(9 * k)
    rt(90)
up()
fd(5 * k)
rt(90)
fd(11 * k)
rt(90)
down()
for i in range(2):
    fd(20 * k)
    rt(90)
    fd(8 * k)
    rt(90)
up()

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * k, y * k)
        dot(3)
done()

# 170
# 189