file = open('test.txt')
s = file.readline()

for l in range(len(s)):
    if l != 'D':
        continue
    for r in range(l, len(s)):
        ps = s[l:r]