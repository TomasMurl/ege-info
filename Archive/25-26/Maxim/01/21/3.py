# Ввести символ. Проверить, является ли он четным (5, 12, 7, 18, 3).
mass = [5, 12, 7, 18, 3]

for i in mass:
    if i % 2 == 0:
        print(i, "even")
    else:
        print(i, "odd")