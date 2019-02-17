#!/usr/bin/env python3

london_co = {
    'r1' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '4451',
    'ios': '15.4',
    'ip': '10.255.0.1'
    },
    'r2' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '4451',
    'ios': '15.4',
    'ip': '10.255.0.2'
    },
    'sw1' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '3850',
    'ios': '3.6.XE',
    'ip': '10.255.0.101',
    'vlans': '10,20,30',
    'routing': True
    }
}

MODEL = input('\nEnter device name: ')

KEYS = list(london_co[MODEL].keys())
KEYS = ','.join(KEYS)
PARAM = input('Enter parameter name('+KEYS+'): ')
PARAM = PARAM.lower()
print(london_co[MODEL].get(PARAM, 'Такого параметра нет'))
