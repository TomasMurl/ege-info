from turtle import *

# Вспомогательный этап
k = 40
screensize(4000, 4000)
tracer(0)
left(90)

# Основная программа
right(90)
for i in range(3):
    right(45)
    forward(10 * k)
    right(45)
right(315)
forward(10 * k)
for i in range(2):
    right(90)
    forward(10 * k)

# Рисование сетки
up()

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * k, y * k)
        dot(4)
done()