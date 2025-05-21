file = open("24-300.txt")
line = file.readline()

max_len = -1000000000
znaki = "+*"
cifri = "0123456789"

for i in range(len(line)):
    if line[i] in znaki:
        continue
    subline = ""
    last = ""
    for j in range(i, len(line) - 1): # 0*0+*02
        if line[j] in znaki and line[j+1] in znaki:
            if len(subline) > max_len and eval(subline) == 0:
                max_len = len(subline)
                print(subline)
            break
        if last in znaki and line[j] == "0" and line[j+1] in cifri:
            subline += line[j]
            if len(subline) > max_len and eval(subline) == 0:
                max_len = len(subline)
                print(subline)
            break
        subline += line[j]
        last = line[j]
print(max_len)