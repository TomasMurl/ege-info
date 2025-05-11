file = open("24-296.txt")
line = file.readline()

# ....[AF....AF.....AF]...... - minimum
# ....A.....A[.....A....A.....]A..... - maximum  
# .... D.... .... ....C .....
sublines = line.split("AF")
minlen = 100000000000
for i in range(len(sublines)):
    subline = sublines[i:i+200]
    real_subline = "D" + "AF".join(subline) + "C"
    if real_subline.count("AF") == 201:
        minlen = min(minlen, len(real_subline))
print(minlen)