from itertools import *

words = "ГЛУБИНА"
c = 0
for i in permutations(words):
    if i[0] != "Г" and i[1] != "Л" and i[2] != "У" and i[3] != "Б" and i[4] != "И" and i[5] != "Н" and i[6] != "А":
        c += 1
print(c)