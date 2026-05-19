from random import randint

m = []
for i in range(10):
    m.append(randint(0, 100))

print(m)

min_m = 101
for i in m:
    if i < min_m:
        min_m = i
print(min_m)