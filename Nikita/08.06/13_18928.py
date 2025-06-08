from ipaddress import *

net = ip_network("192.168.248.176/255.255.255.240", 0)
c = 0
for ip in net:
    ip2 = bin(int(ip))[2:]
    if ip2.count("1") == ip2.count("0"):
        c += 1
print(c)