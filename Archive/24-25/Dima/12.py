stroka = "9" * 81
while "33333" in stroka or "999" in stroka:
    if "33333" in stroka:
        stroka = stroka.replace("33333", "99", 1)
    else:
        stroka = stroka.replace("999", "3", 1)
print(stroka)