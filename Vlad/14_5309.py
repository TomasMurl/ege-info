def perevod(n, osn):
    result = []
    while n != 0:
        result.append(n % osn)
        n = n // osn
    return result[::-1]

c = 4 * 8 ** 3032 + 3 * 16 ** 1956 + 870
c_7 = perevod(c, 7)
print(c_7)
c3 = c_7.count("3")
c1 = c_7.count("1")
print( c3 * 3 - c1 )