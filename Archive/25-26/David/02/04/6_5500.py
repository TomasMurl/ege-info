from turtle import *

# forward(N), fd(N) - вперёд
# backward(N), bk(N) - назад
# right(N), rt(N) - вправо
# left(N), lt(N) - влево
# up() - поднять хвост
# down() - опустить хвост
# goto(x, y) - переместиться в точку
# dot() - поставить точку
# tracer(0) - отключить задержку
# screensize(2000, 2000) - добавить ползунки

# Параметры
tracer(0)
screensize(2000, 2000)
k = 100

left(90)

# Как в задании
for i in range(7):
    fd(10 * k)
    rt(120)

# Рисуем точки
up()
for x in range(-10, 20):
    for y in range(-10, 10):
        goto(x * k, y * k)
        dot(4)
done()