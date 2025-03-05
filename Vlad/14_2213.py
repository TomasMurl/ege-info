def perevod(n, osn):
    result = ""
    while n != 0:
        result = str(n % osn) + result
        n = n // osn
    return result

ch = 9 ** 20 + 3 ** 60 - 15
ch_3 = perevod(ch, 3)
print(ch_3.count("2"))