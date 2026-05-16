from ipaddress import *

net = ip_network('192.168.112.11/255.255.255.128', False)
c = 0
# Все ip в сети net
for ip in net:
    print(c, ip)
    c += 1