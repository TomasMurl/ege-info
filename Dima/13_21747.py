from ipaddress import *

ip = ip_address("84.23.84.23")
for mask in range(1, 32):
    net = ip_network(f"84.23.84.0/{mask}", 0)
    if ip in net:
        print(mask)

