# ## Задание 4. Подсчёт символов
# Дана строка.
#
# Посчитай, сколько раз в ней встречается буква `'a'`.

stroka = "lksdfjkl;wjq;fk;dwjflksadkfnsnvj,asnjkas"

c = 0

for i in stroka:
    if i == "a":
        c = c + 1
print(c)