alf = "0123456789ABCDEFGHIJKLMNOPQRS"

for x in alf:
    s = int("923" + x + "874", 29) + int("524" + x + "6152", 29)
    if s % 28 == 0:
        print(x, s // 28)