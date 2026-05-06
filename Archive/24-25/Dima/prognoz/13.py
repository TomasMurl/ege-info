from ipaddress import *

net = ip_network("97.191.34.206/255.255.255.240", 0)
print(net[-2])