def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

m = []

def convert(n, b):
    r = ''
    while n > 0:
        r += str(n % b)
        n = n // b
    return r[::-1]

for N in range(167, 1000):
    N_3 = convert(N, 3)

    if int(N_3) % 9 == 0:
        N_3 = N_3 + "2"
    else:
        N_3 = N_3 + convert(((sum([int(i) for i in N_3])) % 9), 3)

    R = int(N_3, 3)
    m.append(R)

print(min(m))

# 1. i for i in N_3
# 2. [int(i) for i in N_3]
# 3. sum([int(i) for i in N_3])