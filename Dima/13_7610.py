from ipaddress import *

net = ip_network('94.253.128.0/255.255.128.0')

c = 0
for ip in net:
    ip_2 = bin(int(ip))[2:]
    print(ip, ip_2)
    if ip_2.count("1") % 6 != 0 and ip_2[-3:] == "101":
        c += 1
print(c)