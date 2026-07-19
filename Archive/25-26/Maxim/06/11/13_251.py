from ipaddress import *

rnet = ip_address("111.81.192.0")
for m in range(1, 32):
    net = ip_network(f"111.81.200.27/{m}", False)
    if net[0] == rnet:
        print(m)