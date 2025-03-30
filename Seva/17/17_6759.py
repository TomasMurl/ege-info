# 1. Открыть файл, записать все его данные в массив
# 2. Определение числа, которое нужно по условию (может и не быть)
# 3. Основная проверка

file = open("17-381.txt")
m = []
for line in file:
    m.append(int(line))

max_39_4 = -1000000000
for ch in m:
    if 999 < abs(ch) < 10000 and (abs(ch) % 100 == 39 or str(ch)[-2:] == '39'):
        max_39_4 = max( max_39_4, ch )

c = 0
max_sum = -100000000
for i in range(len(m)-1):
    a = 0 # Сколько четырехзначных в нашей паре
    if 999 < abs(m[i]) < 10000:
        a += 1
    if 999 < abs(m[i+1]) < 10000:
        a += 1
    summa = m[i] + m[i+1]
    if a == 1 and summa ** 2 <= max_39_4 ** 2:
        c += 1
        max_sum = max(max_sum, summa)
print(c, max_sum)