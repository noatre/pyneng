#!/usr/bin/env python3

vlan_input = input('Enter VLAN number: ')

mac_list = []
with open('CAM_table.txt') as f:
    for line in f:
        if line.count('Gi') == 1:
            line = line.replace('DYNAMIC', '')
            line = line.split()
            mac_list.append(line)


for i in mac_list:
    if i[0] == vlan_input:
        print(i)

