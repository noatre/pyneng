#!/usr/bin/env python3

access_template = ['switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk allowed vlan {}']

if_mode = input('\nEnter interface mode (access/trunk): ')
if_num = input('Enter interface type and number: ')
vlan_num = input('Enter vlan(s): ')

template = {'access':access_template, 'trunk':trunk_template}

print('interface '+if_num)
print('\n'.join(template[if_mode]).format(vlan_num))
