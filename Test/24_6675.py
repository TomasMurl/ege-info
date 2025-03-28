file = open("24-263.txt")
s = file.readline()

s = s.split("Y")
max_len = 0

for i in range(len(s)):
    leng = len(s[i])
    c = 0
    for j in range(i + 1, len(s)):
        c += 1
        leng += len(s[j])
        if c == 150:
            max_len = max(leng + c, max_len)
            break
print(max_len)