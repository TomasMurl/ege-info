from ipaddress import *

net = ip_network("139.190.87.229/255.255.248.0", 0)
print(net[-2])