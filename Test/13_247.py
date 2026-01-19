import ipaddress

ip1 = ipaddress.ip_address("118.222.130.140")
ip2 = ipaddress.ip_address("118.222.201.140")

for mask in range(1, 33):
    net1 = ipaddress.ip_network(f"{ip1}/{mask}", 0)
    net2 = ipaddress.ip_network(f"{ip2}/{mask}", 0)

    if net1.network_address == net2.network_address:
        print(net1.netmask)