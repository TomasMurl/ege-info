from ipaddress import *

c = 0
net = ip_network("222.121.128.0/255.255.224.0", 0)
for ip in net:
    ip2 = bin(int(ip))[2:]
    if ip2[-1] == ip2[-2]:
        c += 1
print(c)