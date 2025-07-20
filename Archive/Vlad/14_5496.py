alf = "0123456789A"

for x in alf:
    for y in alf:
        res = int("7"+y+"23"+x+"5", 25) + int("67"+x+"9"+y, 11)
        if res % 131 == 0:
            print(res // 131)