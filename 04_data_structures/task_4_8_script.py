#!/usr/bin/env python3

IP = '192.168.3.1'

ip_template = '''
{0:<8} {1:<8} {2:<8} {3:<8}
'''

IP = IP.split('.')
print(ip_template.format(*IP))

IP[0] = int(IP[0])
IP[1] = int(IP[1])
IP[2] = int(IP[2])
IP[3] = int(IP[3])

ip_template_b = '''
{0:08b} {1:08b} {2:08b} {3:08b}
'''

print(ip_template_b.format(*IP))

