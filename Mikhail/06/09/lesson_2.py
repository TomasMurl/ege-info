# int (целочисленный), float (числа с плавающей запятой), str (строчный), list (массив), bool (булевый)

a = 54
b = 5.3
c = '435'
d = "wadsk"
e = [43, "32", [2, 'sr'], a, b]
f = True # False
g = 0 # 1

# int, float ===============

a = 5
b = 2
print(a, b, a + b, a - b, a / b, a * b)
print(a ** b, a % b, a // b)
print("===================")

# str ======================

a = "pow"
b = "up"
print(a, b, a + b, a * 7)
# 2 * 3 = 2 + 2 + 2
print("===================")

# list =====================

#    0   1   2    3
m = [50, 20, 30, -5]
#    -4  -3  -2   -1
print(m)
print(m[2])
print(m[0] + m[3])

s = "Vanya_2000"
print(s[0] + s[-1])
print("===================")

# срезы в массивах ==========
s = "Информатика"
# s[start:end:step]
print(s[1:11:1], s[::])
print(s[2:], s[:-2])
print(s[::-1])
print(s[::2])
print("===================")

# Условный оператор / ветвление

# if <условие>:
#     <код1>
# else:
#     <код2>
# <код3>

# Возможные условия:
# a < b, a > b, a <= b, a >= b
# a == b, a != b

a = 44
b = 443
if a < b:
    print("a меньше b!")
else:
    print("a больше или равно b!")

if a == b:
    print("а равно b!")
if a != b:
    print("а не равно b!")

#  И   ИЛИ  НЕ
# and, or, not
a, b = 100, 200
if a > b and a < 100:
    print("and выполняется!")

if a > b or a < 100:
    print("or выполняется!")

a = 20
if 0 <= a <= 10:
    print("число a между 0 и 10")