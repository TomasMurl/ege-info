def algorithm(N):
    binary = bin(N)[2:]

    if N % 2 == 0:
        digit_sum = sum(int(d) for d in binary)
        binary_sum = bin(digit_sum)[2:]
        binary = binary + binary_sum
    else:
        binary = '1' + binary + '00'

    R = int(binary, 2)
    return R


for N in range(1, 200):
    R = algorithm(N)
    if R > 215:
        print (f"Ответ: {N}")
        break