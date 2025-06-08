from ipaddress import *

net = ip_network("172.16.80.0/255.255.248.0", 0)
c = 0
for ip in net:
     ip2 = bin(int(ip))[2:]
     if ip2.count("1") % 2 != 0:
         c += 1
print(c)