### Типы данных

## int - целочисленный тип данных
a = 54
a = 4
print(a)
print('============')
# int - операции
a = 5
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b) # float
print(a ** b)

# mod, div -> остаток от деления, целая часть от деления
print(a % b)
print(a // b)
print('============')

## str - строковый тип данных
a = 'dawdwa'
print(a, type(a))

# str - операции
a = 'example'
print(a * 2)
# print(a + 2, a - 2, a / 2) # error
# Конкатенация
a = 'one'
b = 'two'
print(a + b)
print(a + ' eee ' + b)
print('============')

## Полезный пример
a = 5
b = 3
print(str(a) + str(b))
print('============')

## list - массив
m = [20, 30, 'pow', [10, 'qwe']]
print(m)

# Индекс - номер элемента в массиве (у первого элемента индекс - 0)
print(m[2])

# .append(x) - добавить элемент x в конец list (справа)
m.append('Alisa')
print(m)
print('============')

## bool - булевый тип данных (Истина/Ложь)
a = True
b = False
c = True
print(a + b + c)
print('============')

### Ветвление (if-elif-else)

# Структуризация кода
# if < условие1 >:
#     < line1 >
#     < line2 >
#     < line3 >
# elif < условие2 >:
#     < line1 >
#     < line2 >
# elif < условие3 >:
#     < line1 >
#     < line2 >
# else:
#     < line1 >
#     < line2 >
# <line1>

# Условие равенства
a, b = 2, 3
if a == b:
    print("a и b равны друг другу")
else:
    print("a и b не равны друг другу")

print(a == b, type(a == b))
# Условие неравенства
# a > b, a < b, a >= b, a <= b, a != b
if a != b:
    print("a и b не равны друг другу")

# Алгебра логики (and, or)
a, b = 2, 2
if a == b and a > 1:
    print("Да!")
else:
    print("Нет")

a, b = 1, 1
if a == b or a > 1:
    print("Да!")
else:
    print("Нет")

# Условие принадлежности множеству (in)
a = [1, 2, 3, 4]
b = 4
if b in a:
    print("Да, b содержится в a")

# Инверсия условия (not)
a = [1, 2, 3, 4]
b = 54
if b not in a:
    print("Да, b не содержится в a")
