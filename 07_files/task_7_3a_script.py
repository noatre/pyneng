#!/usr/bin/env python3

mac_list = []
mac_list_vlan_as_key = []
with open('CAM_table.txt') as f:
    for line in f:
        if line.count('Gi') == 1:
            line = line.replace('DYNAMIC', '')
            line = line.split()
            mac_list.append(line)
            mac_list_vlan_as_key.append(line[0])

mac_list_vlan_as_key = set(mac_list_vlan_as_key)
mac_list_vlan_as_key = list(mac_list_vlan_as_key)
mac_list_vlan_as_key.sort()

for vlan in mac_list_vlan_as_key:
    for i in mac_list:
        if i[0] == vlan:
            print(i)

