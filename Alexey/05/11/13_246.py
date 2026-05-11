from ipaddress import ip_address, ip_network

ip = ip_address('124.128.112.142')
ip_net = ip_address('124.128.64.0')
print(bin(int(ip))[2:])
print(bin(int(ip_net))[2:])

