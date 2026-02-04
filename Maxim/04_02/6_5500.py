from turtle import *

# fd(N) - вперёд
# back(N) - назад
# rt(N) - направо
# lt(N) - налево
# up() - поднять хвост
# down() - опустить хвост
# done() - остановиться и не закрывать лист
# goto(x, y) - переместитсья в точку
# dot(4) - поставить точку
# tracer(0) - отключить задержку
# screensize(4000, 4000) - добавить ползунки

# Параметры
tracer(0) #
screensize(4000, 4000)
k = 60 #
lt(90)

# Как в задании
for i in range(7):
    fd(10 * k)
    rt(120)

# Рисуем точки
up()
for x in range(-20, 20): #
    for y in range(-20, 20): #
        goto(x * k, y * k)
        dot(4)
done()