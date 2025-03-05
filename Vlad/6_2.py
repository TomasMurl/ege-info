from turtle import *
print(24 + 16 * 2 ** (0.5))

lt(90)
k = 100
tracer(0)
screensize(4000, 4000)
for i in range(5):
    for j in range(2):
        fd(3 * k)
        lt(45)
        fd(3 * k)
        rt(90)
    right(180)

up()

for x in range(-10, 10):
    for y in range(-10, 10):
        goto(x * k, y * k)
        dot(5)
done()