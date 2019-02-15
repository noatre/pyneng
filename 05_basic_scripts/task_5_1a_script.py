#!/usr/bin/env python3

IP = input('\nВведите IP в формате x.x.x.x/x:\n')
IP = IP.replace('/','.')
IP = IP.split('.')
#IP[-1] = IP[-1].split('/')
MASK = IP.pop(-1)
MASK = int(MASK)

# Конвертируем строки в числа
IP[0] = int(IP[0])
IP[1] = int(IP[1])
IP[2] = int(IP[2])
IP[3] = int(IP[3])

# Делаем из адреса сеть
#IP_B = [bin(int(IP[0])), bin(int(IP[1])), bin(int(IP[2])), bin(int(IP[3]))]

## Делаем строку в двоичном виде
IP_STR = '{0:08b}{1:08b}{2:08b}{3:08b}'.format(*IP)
IP_NET_STR = IP_STR[0:MASK]+'0'*(32-MASK)
IP_10_LIST = [int(IP_NET_STR[0:8], 2), int(IP_NET_STR[8:16], 2), int(IP_NET_STR[16:24], 2), int(IP_NET_STR[24:32], 2)]
#print(IP_10_LIST)

# Вывод адреса
print('\nNetwork:')
ip_print = '''
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''
print(ip_print.format(*IP_10_LIST))

MASK_B = ('1'*MASK)+('0'*(32-MASK))

# Вывод маски
print('\nMask:')
print('\{}'.format(MASK))
MASK_B_LIST = [MASK_B[0:8], MASK_B[8:16], MASK_B[16:24], MASK_B[24:32]]
MASK_10_LIST = [int(MASK_B[0:8], 2), int(MASK_B[8:16], 2), int(MASK_B[16:24], 2), int(MASK_B[24:32], 2)]

print(ip_print.format(*MASK_10_LIST))
