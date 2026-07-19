## Применение изменения типов
a = 20841243
a = str(a) # "20841243"
b = a.count("2")

# print(b // 2)

## Массивы - упорядоченный набор объектов

a = [ 10, 20, 30, [1, 2], "ser" ]
# print(a, a[0], a[2])

b = "wqe2lkemlk23ljrbjbhjd3jk"
# print(b[0])

# print(len(a), len(b))

a = [10, 20, 30, 40, 12, 43, 54]
# print(a[len(a) - 1])
# print(a[-2], b[-2])

## Срезы

a = [100, 200, 300, 400, 500, 600]

# a[start:end:step]

# print(a[0:6])
# print(a[2:4])
# print(a[2:])

a = "poqwkeqwqwkeqwpekqpw"
# print(a[1:len(a) - 1])

## Ветвление: if-else

a = 53
b = 21
# if a == b:
#     print("Больше b!")
#     print("А пришло к нам", a)
# else:
#     print("Не больше b!")
# print("Закончили!")

# >, <, >=, <=
# == - "равно ли", позволяет сравнивать объекты: if a == b:
# != - "не равно ли", позволяет узнать неравенство объектов: if a != b:
# in / not in - "содержит ли / не содержит ли", позволяет нам узнать наличие чего-то в чем-то: if a in b:

a = "pwower"
# if "po" in a:
#     print("Содержится!")
# else:
#     print("Не содержится!")

a = "АОЕИ"
b = "Е"
# if b not in a:
#     print("Гласная!")
# else:
#     print("Согласная!")

## Булевый тип данных (bool)
a = True # 1
b = False # 0

# if a:
#     print("a это True")