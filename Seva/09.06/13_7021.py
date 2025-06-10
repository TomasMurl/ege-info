from ipaddress import *

for m in range(0, 33):
    net = ip_network(f"134.73.209.97/{m}", 0)
    if str(net.network_address) == "134.73.192.0":
        print(m, net.netmask)
        break
