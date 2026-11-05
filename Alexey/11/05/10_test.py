from ipaddress import *

net = ip_network('192.168.108.157/255.255.255.192', False)
c = 0
print(net)
for ip in net:
    a, b, c, d = str(ip).split('.') # => ['192', '168', ...]
    c += 1