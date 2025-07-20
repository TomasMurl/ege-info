from turtle import *

tracer(0) # быстрая отрисовка
screensize(2000, 2000) # для ползунков
k = 20 # масштабирование
lt(90) # влево

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
up() # чтобы не тащился хвост

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * k, y * k) # переместиться в точку (x,y)
        dot(3) # нарисовать точку
done() # чтобы не закрывалось окно после завершения