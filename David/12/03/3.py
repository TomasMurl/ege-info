# Максимум из трёх чисел
# Ввести три числа. Вывести самое большое.

a = int(input("Введите 1 число: "))
b = int(input("Введите 2 число: "))
c = int(input("Введите 3 число: "))

# if a > b and a > c:
#     print(a)
# if b > a and b > c:
#     print(b)
# if c > a and c > b:
#     print(c)

# int - превращает строку в число
# print - выводит на экран
# range(a, b) - набор чисел от a до b (не включая b)
# max - находит максимальное из данных чисел

maxi = max(a, b, c)
print(maxi)