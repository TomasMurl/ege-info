alf = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for x in alf[:22]:
    v = int(f"82934{x}2", 21) + int(f"2924{x}{x}7", 21) + int(f"67564{x}8", 21)
    if v % 20 == 0:
        print(x, v // 20)