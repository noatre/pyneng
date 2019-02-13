#!/usr/bin/env python3

CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'

CONFIG_SPLIT = CONFIG.split()
print(CONFIG_SPLIT[-1].split(','))
