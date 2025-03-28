file = open("24-298.txt")
s = file.readline()
import re
matches = re.findall(r"([1-9][0-9]*([-*][1-9][0-9]*)*)", s)
max_len = 0
for match in matches:
    max_len = max(max(map(len, match)), max_len)
print(max_len)