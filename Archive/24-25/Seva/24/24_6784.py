file = open("24-263.txt")

s = file.readline()

max_len = 0
for i in range(len(s)-1):
    for j in range(i, len(s)-1):
        if s[j] == "P" and s[j+1] != "C":
            len()