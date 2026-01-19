import ipaddress

target_ip = ipaddress.ip_address("111.81.208.27")
target_net = ipaddress.ip_address("111.81.192.0")
for mask in range(1, 33):
    net = ipaddress.ip_network(f"111.81.192.0/{mask}", 0)
    if target_ip in net and net.network_address == target_net:
        mask = ipaddress.ip_network(f"0.0.0.0/{mask}").netmask
        print(mask)
