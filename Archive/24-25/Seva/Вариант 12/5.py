c = 0
for N in range(0, 255):
    N_2 = bin(N)[2:].zfill(8)
    result = ''
    for i in N_2:
        if i == "0":
            result += "1"
        else:
            result += "0"
    if int(result, 2) % 5 == 0:
        result = "100" + result[3:]
    else:
        result = "101" + result[3:]
    R = int(result, 2)
    if R == 180:
        c += 1
print(c)