from ipaddress import *

net = ip_network("94.149.96.0/255.255.224.0")

c = 0
for ip in net:
    ip_2 = bin(int(ip))[2:]
    if ip_2.count("1") % 3 == 0 and ip_2[-2:] == "11":
        c += 1
print(c)