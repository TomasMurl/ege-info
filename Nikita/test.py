a = 16
dels = {1, a}

for i in range(2, int(a ** 0.5) + 1):
    if a % i == 0:
        dels.add(i)
        dels.add(a // i)
dels = sorted(dels)

print(dels)