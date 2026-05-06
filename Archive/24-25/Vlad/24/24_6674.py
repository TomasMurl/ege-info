file = open("24-263.txt")
line = file.readline()

# ...Y...Y...Y....Y....Y....
minlen = 100000000000000000
sublines = line.split("Z")
for i in range(len(sublines)):
    subline = sublines[i:i+119]
    real_subline = "Z" + "Z".join(subline) + "Z"
    if real_subline.count("Z") >= 120:
        minlen = min(minlen, len(real_subline))
print(minlen)