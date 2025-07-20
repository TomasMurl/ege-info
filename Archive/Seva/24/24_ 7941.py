file = open("24-309.txt")
line = file.readline()

podlines = line.split("FSRQ")
max_len = 0
for i in range(len(podlines)):
    podstroka = podlines[i:i+81]
    result = "FSRQ".join(podstroka)
    max_len = max(max_len, len(result) + 3 * 2)
print(max_len)