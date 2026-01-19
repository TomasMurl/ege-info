from ipaddress import ip_network

mask = sum(map(lambda x: bin(int(x))[2:].count("1"), "255.255.224.0".split(".")))
net = ip_network(f"10.8.248.131/{mask}", 0)
print(net.network_address)