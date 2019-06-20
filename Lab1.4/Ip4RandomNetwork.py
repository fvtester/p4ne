import random
import ipaddress
#from ipaddress import IPv4Network

class IPv4RandomNetwork(ipaddress.IPv4Network):
    def __init__(self):
        address=random.randint(0x0B000000,0xDF000000)
        mask = random.randint(8, 24)
        #print(str(address)+'/' + str(mask))
        address1 = ipaddress.IPv4Address(address)
        #print(dir(address1))
        #print(str(address1)+'/' + str(mask))
        ipaddress.IPv4Network.__init__(self, str(address1)+'/' + str(mask),strict=False)
    def regular(self):
        #print(self.is_global)
        return self.is_global
    def key_value1(self, address ):
        m=int(self.netmask)
        return int(address)+m

    def key_value1(self, address):
        m = int(self.netmask)
        return int(address) + m

    def key_value(self):
        m = int(self.netmask)
        n=int(self.network_address)
        #print(int(str(m) + str(n)))
        return (int(str(m) + str(n)))

def f(a):
    return a.key_value()

a=IPv4RandomNetwork()
print(a.regular())
#print(list(a.hosts()))
#for host in a.hosts():
#    print(a.key_value1(host))
networks=[]
for i in range(10):
    networks.append(IPv4RandomNetwork())
print(f(networks[0]))
networks_sorted=sorted(networks, key=f)
print(networks_sorted)