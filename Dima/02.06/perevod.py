# 8_10 -> 1000_2
# 
def perevod(n, osn):
    res = ''
    while n > 0:
        res = str(n % osn) + res
        n = n // osn
    return res

def perevod_2(n, osn):
    res = []
    while n > 0:
        res.append(n % osn)
        n = n // osn
    return res[::-1]

print(perevod(73223, 23))
print(perevod_2(73223, 23)) # 609D
m = perevod_2(73223, 23)
c = sum([1 for x in m if x > 8])
print(c)
# m = perevod_2(73223, 23)
# for i in m:
#     if i > 8:
#         c += 1