alf = "0123456789ABCDE"
for x in alf:
    n1 = "123" + x + "5"
    n2 = "1" + x + "233"
    n1 = int(n1, 15)
    n2 = int(n2, 15)
    s = n1 + n2
    if s % 14 == 0:
        print(s // 14)
        break