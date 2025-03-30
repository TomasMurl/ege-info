from itertools import product

alf = "01234567"

words = product(alf, repeat=6)
c = 0
for word in words:
    flag = True
    if word[0] == "0":
        continue
    if word.count('4') != 2:
        continue
    for i in range(len(word) - 1):
        if word[i] == '4' and word[i+1] == '4':
            flag = False
    if word.count('0') > 1 or word.count('1') > 1 or word.count('2') > 1 or word.count('3') > 1 or word.count('5') > 1 or word.count('6') > 1 or word.count('7') > 1:
        flag = False
    f = 0
    for b in word:
        if b == '4' and f == 0:
            f = 1
            continue
        if b == '4' and f == 1:
            f = 0
            continue
        if f == 1:
            if int(b) < 5:
                flag = False
    if flag:
        print(str(word))
        c += 1
print(c)