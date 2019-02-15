#!/usr/bin/env python3

IP = input('\nВведите IP в формате x.x.x.x/24:\n')
IP = IP.replace('/','.')
IP = IP.split('.')
#IP[-1] = IP[-1].split('/')
MASK = IP.pop(-1)

IP[0] = int(IP[0])
IP[1] = int(IP[1])
IP[2] = int(IP[2])
IP[3] = int(IP[3])

print('\nNetwork:')
ip_print = '''
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''
print(ip_print.format(*IP))
#print(IP)
#print(MASK)
MASK = int(MASK)
MASK_B = ('1'*MASK)+('0'*(32-MASK))

print('\nMask:')
print('\{}'.format(MASK))
#print(MASK_B)
MASK_B_LIST = [MASK_B[0:8], MASK_B[8:16], MASK_B[16:24], MASK_B[24:32]]
MASK_10_LIST = [int(MASK_B[0:8], 2), int(MASK_B[8:16], 2), int(MASK_B[16:24], 2), int(MASK_B[24:32], 2)]

print(ip_print.format(*MASK_10_LIST))
