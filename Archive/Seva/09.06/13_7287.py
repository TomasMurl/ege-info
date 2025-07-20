from ipaddress import *

for m in range(0, 33):
    net1 = ip_network(f"154.63.206.129/{m}", 0)
    # net2 = ip_network(f"154.63.100.75/{m}", 0)
    ip = ip_address("154.63.100.75")
    if ip not in net1:
        print(net1.netmask)
        break
    # if str(net1.network_address) != str(net2.network_address):
    #     print(net1.netmask)
    #     break