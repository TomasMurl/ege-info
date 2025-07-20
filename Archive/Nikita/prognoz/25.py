def get_dels(n):
    dels = {1, n}
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            dels.add(i)
            dels.add(n // i)
    return sorted(dels)

c = 0
for n in range(2_900_000, 10_000_000):
    dels = get_dels(n)
    len_dels_1 = len(get_dels(dels[1]))
    len_dels_2 = len(get_dels(dels[2]))
    if len(dels) == 4 and len_dels_1 == 2 and len_dels_2 == 2: про
        if str(dels[1]).count('0') == 1 and str(dels[2]).count('0') == 1: # проверяем, что в каждом делителе у нас только один "0"
            c += 1
            print(n, dels[2])
            if c == 5: # проверяем, что выводим только 5 первых чисел, потом брейкаем
                break