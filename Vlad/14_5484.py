alf = "0123456789ABCDEFG"

for x in alf:
    o1_17 = "9759" + x
    o2_17 = "3" + x + "108"
    res = int(o1_17, 17) + int(o2_17, 17)
    if res % 11 == 0:
        print(res // 11)
        break