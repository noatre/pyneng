#!/usr/bin/env python3

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_route.split()
print("Protocol: ospf_route[0]\nPrefix: 10.0.24.0/24\nAD/Metric: 110/41\nNext-Hop: 10.0.13.3\nLast update: 3d18h\nOutbound Interface: FastEthernet0/0\n")
