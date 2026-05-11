from ipaddress import ip_address, ip_network

ip = ip_address('111.81.208.27')
print(bin(int(ip))[2:])
net = ip_address('111.81.192.0')
print(bin(int(net))[2:])