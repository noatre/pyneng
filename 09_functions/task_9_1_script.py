#!/usr/bin/env python3

def generate_access_config(access):
    '''
    access - словарь access-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/12':10,
          'FastEthernet0/14':11,
          'FastEthernet0/16':17}

    Возвращает список всех портов в режиме access
    с конфигурацией на основе шаблона
    '''
    access_template = ['switchport mode access',
                       'switchport access vlan',
                       'switchport nonegotiate',
                       'spanning-tree portfast',
                       'spanning-tree bpduguard enable']

    access_dict = []

    for intf, vlan in access.items():
        access_dict.append('interface' + intf)
        for command in access_template:
            if command.endswith('access vlan'):
                access_dict.append('{} {}'.format(command, vlan))
            else:
                access_dict.append('{}'.format(command))

    print(access_dict)

access_dict = { 'FastEthernet0/12':10,
                'FastEthernet0/14':11,
                'FastEthernet0/16':17,
                'FastEthernet0/17':150 }


generate_access_config(access_dict)
