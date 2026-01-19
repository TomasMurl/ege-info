import ipaddress

mask_address = "255.255.248.0"
mask = sum(map(lambda x: bin(int(x))[2:].count("1"), mask_address.split(".")))
net = ipaddress.ip_network(f"139.190.87.229/{mask}", 0)
print(net[-2])