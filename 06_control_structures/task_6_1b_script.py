#!/usr/bin/env python3

ip_input = input('Введите IP адрес X.X.X.X: ')
ip_incorrect = True

while ip_incorrect:
    ip_input = ip_input.split('.')
    ip = []
    for i in ip_input:
     if not i.isdigit():
        print('Incorrect IPv4 address')
        ip_input = input('Введите IP адрес X.X.X.X: ')
        break
     else:
         if 0<=int(i)<=255:
            ip.append(int(i))
         else:
             print('Incorrect IPv4 address')
             ip_input = input('Введите IP адрес X.X.X.X: ')
             break
    if len(ip) == 4:
        ip_incorrect = False
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
    else:
        print('Incorrect IPv4 address')
        ip_input = input('Введите IP адрес X.X.X.X: ')
