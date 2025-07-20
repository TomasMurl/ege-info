from turtle import *

tracer(0)
screensize(2000, 2000)
k = 20
left(90)
x = 5
fd(3 * k)
for i in range(x):
    for j in range(2):
        fd(x * k)
        rt(90)
    fd(x * k)
    lt(90)
    fd(k)
    lt(90)
bk(3 * k)
up()

for x in range(0, 200):
    for y in range(-10, 10):
        goto(x * k, y * k)
        dot(3)
done()

results = []
for x in range(100):
    if x*((x-1)*(x+2)+2) < 250000:
        results.append(x)
print(max(results))