from turtle import *

Turtle()
# up()
# down()
# forward(x) - fd(x)
# backward(x) - bk(x)
# right(a) - rt(a)
# left(a) - lt(a)

# goto(x,y) - переместиться в точку
# dot(w) - поставить точку
# done() - закончить рисование и не закрывать шаблон

# tracer(0) - убрать задержку перед рисованием
# screensize(2000, 2000) - добавить ползунки на холст

lt(90)

for _ in range(2):
    fd(10)
    rt(90)
    fd(20)
    rt(90)
up()
fd(15)
rt(90)
bk(10)
lt(90)
down()
for _ in range(2):
    fd(20)
    rt(90)
    fd(40)
    rt(90)