file = open("17-426.txt")
m = []
for line in file:
    m.append(int(line))

max_43 = -10000000000
for i in m: # -3143
    if str(i)[-2:] == "43" and 9999 < abs(i) < 100000:
        max_43 = max(max_43, i)

c = 0 # счетчик для удовлетворяющих троек
min_sum_kv = 1000000000
for i in range(len(m) - 2):
    p = 0 # счетчик чисел тройки, которые 5знач и оканч на 43
    if 9999 < abs(m[i]) < 100000 and str(m[i])[-2:] == "43":
        p = p + 1
    if 9999 < abs(m[i+1]) < 100000 and str(m[i+1])[-2:] == "43":
        p = p + 1
    if 9999 < abs(m[i+2]) < 100000 and str(m[i+2])[-2:] == "43":
        p = p + 1
    summa_kv = m[i] ** 2 + m[i+1] ** 2 + m[i+2] ** 2
    if p > 0 and summa_kv <= max_43 ** 2:
        c = c + 1
        min_sum_kv = min(min_sum_kv, summa_kv)
print(c, min_sum_kv)