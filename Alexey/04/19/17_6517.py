with open('17-374.txt') as f:
    m = list(map(int, f.readlines()))

min_2 = min(x for x in m if x % 2 == 0)

c = 0
min_sum = 20000
for i in range(len(m) - 2):
    # Важное второе условие "между элементами пары есть ровно один элемент"
    # в сути это задание на самом деле на тройки чисел
    # и мы должны проверить делимость среднего числа на min_2
    if ((m[i] % 2 == 0 and m[i+2] % 2 == 1) or
        (m[i] % 2 == 1 and m[i+2] % 2 == 0)) and m[i+1] % min_2 == 0:
        c += 1
        min_sum = min(min_sum, m[i] + m[i+2])
print(c, min_sum)