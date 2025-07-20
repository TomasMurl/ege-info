file = open("24-212.txt")
line = file.readline()

sogl = "BCD"
gl = "AO"
max_len = -100000000000

for i in range(len(line)):
    current_count = 0
    for j in range(i, len(line) - 1, 2):
        if line[j] in gl and line[j+1] in sogl:
            current_count += 1
        else:
            max_len = max(current_count, max_len)
            break
print(max_len)
        