#!/usr/bin/env python3

mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']

mac_cisco = []

for addr in mac:
    mac_cisco.append('.'.join(addr.split(':')))

print(mac_cisco)
