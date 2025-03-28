f = open("27-p00b.txt")
dots = []
for line in f:
    dots.append([i for i in map(float, line.replace(",", ".").split("\t"))])

def leng(dot1, dot2):
    return pow(pow(dot1[0] - dot2[0], 2) + pow(dot1[1] - dot2[1], 2), 0.5)

cls1 = []
cls2 = []
cls3 = []
for dot in dots:
    if dot[0] < 2.5:
        cls1.append(dot)
    elif dot[1] > 7:
        cls2.append(dot)
    else:
        cls3.append(dot)

cntr1 = []
min_lengs = float("inf")
for i in range(len(cls1)):
    sum_lengs = 0
    for j in range((len(cls1))):
        sum_lengs += leng(cls1[i], cls1[j])
    if sum_lengs < min_lengs:
        min_lengs = sum_lengs
        cntr1 = cls1[i]

cntr2 = []
min_lengs = float("inf")
for i in range(len(cls2)):
    sum_lengs = 0
    for j in range((len(cls2))):
        sum_lengs += leng(cls2[i], cls2[j])
    if sum_lengs < min_lengs:
        min_lengs = sum_lengs
        cntr2 = cls2[i]

cntr3 = []
min_lengs = float("inf")
for i in range(len(cls3)):
    sum_lengs = 0
    for j in range((len(cls3))):
        sum_lengs += leng(cls3[i], cls3[j])
    if sum_lengs < min_lengs:
        min_lengs = sum_lengs
        cntr3 = cls3[i]

print((cntr1[0] + cntr2[0] + cntr3[0])/3*10000, (cntr1[1] + cntr2[1] + cntr3[1])/3*10000 )
    
print(cntr1, cntr2, cntr3)