from ipaddress import *
net = ip_network("186.215.243.5/255.255.192.0", 0)
print(net[-2])