#!/usr/bin/env python3

ip_input = input('Введите IP адрес X.X.X.X: ')
ip_input = ip_input.split('.')
ip = []
a = 0
for i in ip_input:
 if i.isdigit():
     if 0<=int(i)<=255:
        ip.append(int(i))
        a = a + 1
     else:
         print('Incorrect IPv4 address')
         break
 else:
    print('Incorrect IPv4 address')
    break
if len(ip) == 4 and a == 4:
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
elif a == 1:
    print('Incorrect IPv4 address')
