from ipaddress import *

net = ip_network('172.16.168.0/255.255.248.0')
c = 0
for ip in net:
    ip_2 = bin(int(ip))[2:].zfill(32)
    if ip_2.count('1') % 5 != 0:
        c += 1
print(c)