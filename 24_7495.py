file = open("24-296.txt")
s = file.readline()
while "CD" in s:
    s = s.replace("CD", "C D")
s = s.split(" ")
max_len = 0
for i in range(len(s)):
    leng = len(s[i])
    c = 0
    for j in range(i + 1, len(s)):
        c += 1
        leng += len(s[j])
        if c == 160:
            max_len = max(max_len, leng)
            break
print(max_len)