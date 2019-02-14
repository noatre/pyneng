#!/usr/bin/env python3

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_route = ospf_route.split()

for i in ospf_route:
# ospf_route[i].strip(',')
 print(i.strip(','))

 #print("Protocol: ospf_route[0]\nPrefix: 10.0.24.0/24\nAD/Metric: 110/41\nNext-Hop: 10.0.13.3\nLast update: 3d18h\nOutbound Interface: FastEthernet0/0\n")

route_template = '''
Protocol:               {}
Prefix:                 {}
AD/Metric:              {}
Next-Hop:               {}
Last update:            {}
Outbound Interface:     {}
'''

if ospf_route[0] == 'O':
    ospf_route[0] = 'OSPF'

ospf_route.remove('via')
#ospf_route = tuple(ospf_route)
#print(route_template.format(ospf_route))
print(route_template.format(*ospf_route))
#print(ospf_route)
