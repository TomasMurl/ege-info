alf = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for x in alf[:27]:
    s = int(f"2107{x}792", 27) + int(f"565{x}211", 27)
    if s % 26 == 0:
        print(x, s // 26)