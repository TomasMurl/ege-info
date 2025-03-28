file = open("24-296.txt")
s = file.readline()
while "CD" in s:
    s = s.replace("CD", "C D")
s = s.split(" ")
max_len = 0
for i in range(len(s)-161):
    ps = ''.join(s[i:i+161])
    max_len = max(max_len, len(ps))
print(max_len)