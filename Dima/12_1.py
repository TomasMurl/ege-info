stroka = "8" * 83
while "111" in stroka or "88888" in stroka:
    if "111" in stroka:
        stroka = stroka.replace("111", "88", 1)
    else:
        stroka = stroka.replace("88888", "8", 1)
print(stroka)