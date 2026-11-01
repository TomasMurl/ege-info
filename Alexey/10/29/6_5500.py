from turtle import *

# forward(), fd()
# backward(), bk()
# right(), rt()
# left(), lt()
# up(), down()
# goto(x, y)
# dot(4)
# tracer(0) - отключить задержку
# screensize(4000, 4000)

# 1 настройка
k = 80
screensize(4000, 4000)
tracer(0)
lt(90)

# 2 переписывание условия
for i in range(7):
    fd(10 * k)
    rt(120)

up()
# 3 отрисовка сетки
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * k, y * k)
        dot(4)
done()