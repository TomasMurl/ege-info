alf = '0123456789ABCDEFGHIJKL'

for x in alf:
    s = int("325" + x + "684", 22) + int("279" + x + "249", 22) + int("138" + x + "848", 22)
    if s % 21 == 0:
        print(x, s // 21)