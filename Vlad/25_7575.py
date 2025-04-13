def find_dels(n):
    dels = {1, n}
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            dels.add(i)
            dels.add(n // i)
    return sorted(dels)

c = 0
for i in range(800000, 10000000):
    dels = find_dels(i)
    flag = False
    del_9 = 0
    for d in dels:
        if str(d)[-1] == "9" and d != i and d != 9:
            flag = True
            del_9 = d
            break
    if flag:
        print(i, del_9)
        c += 1
    if c == 5:
        break