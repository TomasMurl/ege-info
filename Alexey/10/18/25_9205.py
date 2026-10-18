def find_dels(x):
    d = {1, x}
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)

c = 0
for n in range(2626695891, 3000695891):
    dels = find_dels(n)
    if len(dels) == 3:
        if str(dels[1]).count('67') == 1:
            print(n, dels[1])
            c += 1
    if len(dels) == 4:
        if str(dels[1]).count('67') == 1 and str(dels[2]).count('67') == 1:
            print(n, dels[1])
            c += 1
    if c == 5:
        break