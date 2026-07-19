from ipaddress import *

net = ip_network("172.16.160.0/255.255.240.0", False)
c = 0
for ip in net:
    ip_2 = bin(int(ip))[2:].zfill(32)
    if ip_2.count("1") % 2 == 0:
        c += 1
print(c)
