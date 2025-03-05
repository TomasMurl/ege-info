min_ch = 1000
for n in range(101, 1000):
    stroka = "3" * n
    cur_str = len(stroka)
    while "111" in stroka or "333" in stroka:
        if "111" in stroka:
            stroka = stroka.replace("111", "3", 1)
        else:
            stroka = stroka.replace("333", "1", 1)
            
    if int(stroka) < min_ch:
        min_ch = int(stroka) 
        print(int(stroka), cur_str)