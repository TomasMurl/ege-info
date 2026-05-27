# IDE - среда разработки
# VSCode, Intellij IDEA

# PyCharm

### Типы данных
## int - integer - целочисленный тип данных
a = 123
b = 50
c = a + b

# f(x) = x^2 + 4
print(c)
print(a+b,a-b,a*b,a/b)

# 15 разделил на 4
# / -> 3.75 - обычное деление
# // -> 3 - целая часть от деления
# % -> 1 - остаток от деления

print(a/b,a//b,a%b)
print("=================")
## float - число с плавающей запятой (нецелые)
a = 2.45
b = 3.8
print(a+b,a-b,a*b,a/b)
print(a/b,a//b,a%b)

print(4/4, type(4/4)) # обычное деление в Python всегда возвращает float
print("=================")

## str - string - строчный тип данных
a = 'text'
b = "pow"
c = 'qwe'
print(a+b+c) # конкатенация строк
# print(a-b)
print(a * 4) # str * int
a = 153
b = 42
print(type(a), type(b))
print(b + a)