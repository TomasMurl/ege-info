from ipaddress import *

net = ip_network('192.168.159.86/255.255.252.0', False)
print(net, net[0])

# net[0] - сама сеть
#
# net[-2] - последний ip компьютера
# net[-1] - широковещательный адрес