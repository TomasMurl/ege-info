file = open("24-296.txt")

s = file.readline()

min_len = 100000000
s = s.split("AF")
for i in range(len(s)-200):
    podstroka = ''.join(s[i:i+200])
    min_len = min(min_len, len(podstroka)+201*2)
print(min_len)