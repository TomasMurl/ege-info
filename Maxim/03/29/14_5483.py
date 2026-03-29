alf = '0123456789ABCDE'

for x in alf:
    s = int(f"123{x}5", 15) + int(f"1{x}233", 15)
    if s % 14 == 0:
        print(x, s // 14)
        break