#!/usr/bin/env python3

ip = input('Введите IP адрес: ')
ip = ip.split('.')

for i in range(4):
 ip[i] = int(ip[i])

if ip[0] < 224 and ip[0] > 0:
 print('unicast')
elif ip[0] > 223 and ip[0] < 255:
 print('multicast')
elif ip[0] == ip[1] == ip[2] == ip[3] == 255:
 print('local broadcast')
elif ip[0] == ip[1] == ip[2] == ip[3] == 0:
 print('unassigned')
else:
 print('unused')
