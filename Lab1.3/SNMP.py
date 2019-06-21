from pysnmp.hlapi import * # Импортировать только High-level API

result = getCmd(SnmpEngine(),
	CommunityData('public', mpModel=0),
	UdpTransportTarget(('10.31.70.107', 161)),
	ContextData(),
	ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))
result2 = nextCmd(SnmpEngine(),
	CommunityData('public', mpModel=0),
	UdpTransportTarget(('10.31.70.107', 161)),
	ContextData(),
	ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2')), lexicographicMode=False) # Не идти в глубину
#result2 = nextCmd('SNMPv2-MIB', 'sysDescr', '10.31.70.107', 161, 0, lexicographicMode=False) # Не идти в глубину

print(result)
print(result2)
for i in result:
    for j in i[3]:
        print(j)

for z in result2:
    for y in z[3]:
        print(y)

#snmp_object = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0) # По имени MIB-переменной

#snmp_object = ObjectIdentity('1.3.6.1.2.1.2.2.1.2') # По значению MIB-переменной

