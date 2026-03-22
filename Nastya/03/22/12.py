a = 24
b = 216
d = 0  # Делитель

for i in range(2, a):
    if a % i == 0 and b % i == 0:
        d = i
print(d)