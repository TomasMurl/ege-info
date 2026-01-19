import ipaddress

target_ip = ipaddress.ip_address("124.128.112.142")
target_network = ipaddress.ip_address("124.128.64.0")

for mask in range(1, 33):
    net = ipaddress.ip_network(f"124.128.64.0/{mask}", 0)
    if target_ip in net and net.network_address == target_network:
        print(net.netmask)