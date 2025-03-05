from ipaddress import *

net = ip_network("172.16.168.0/255.255.248.0")

c = 0
for ip in net:
    ip_2 = bin(int(ip))[2:]
    sum_1 = ip_2.count("1")
    if sum_1 % 5 != 0:
        c += 1
print(c)