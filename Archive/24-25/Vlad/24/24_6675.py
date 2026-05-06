file = open("24-263.txt")
line = file.readline()

# ...Y...Y...Y....Y....Y....
maxlen = 0
sublines = line.split("Y")
for i in range(len(sublines)):
    subline = sublines[i:i+151]
    real_subline = "Y".join(subline)
    maxlen = max(maxlen, len(real_subline))
print(maxlen)