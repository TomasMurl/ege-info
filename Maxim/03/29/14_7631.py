alf = '0123456789ABCDEFGHI'

for x in alf:
    s = int(f"98897{x}21", 19) + int(f"2{x}923", 19)
    if s % 18 == 0:
        print(x, s // 18)