with open('17-426.txt') as f:
    m = list(map(int, f))

max_43 = max(x for x in m if str(x)[-2:] == '43' and 9999<abs(x)<100000)

cnt = 0
min_sum = 99999999999
for i in range(len(m) - 2):
    a, b, c = m[i], m[i + 1], m[i + 2]
    if (str(a)[-2:] == '43' and 9999<abs(a)<100000) or (str(b)[-2:] == '43' and 9999<abs(b)<100000) or (str(c)[-2:] == '43' and 9999<abs(c)<100000):
        if (a**2+ b**2 + c**2) <= max_43**2:
            cnt += 1
            min_sum = min(min_sum, a**2 + b**2 + c**2)
print(cnt, min_sum)