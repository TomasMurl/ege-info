# Количество положительных чисел
# Ввести N чисел по очереди. Посчитать, сколько из них положительные.

# a = [1, 2, 3]
# print(a[1])

numbers = []
while True:
    a = input("Введите число: ")
    if a == "":
        break
    numbers.append(int(a))
    print(numbers)

c = 0
for n in numbers:
    if n > 0:
        c = c + 1

print(c)