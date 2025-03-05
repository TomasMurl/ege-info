# net - 227.31.A.128
# 224 - 1110 0000
# 139 - 1000 1011
# 128 - 1000 0000

import ipaddress

for A in range(256):
    net_str = "227.31." + str(A) + ".128/255.255.255.224"
    net = ipaddress.ip_network(net_str)
    results = []
    for ip in net:
        ip_2 = bin(int(ip))[2:].zfill(32) # "10010101 01011010 101001101 0010101"
        le0 = ip_2[:16].count("0")
        pr0 = ip_2[16:].count("0")
        if le0 <= pr0:
            results.append(True)
        else:
            results.append(False)
    if all(results):
        print(A)