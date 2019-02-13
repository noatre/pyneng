#!/usr/bin/env python3

command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'

command1 = command1.split()
command2 = command2.split()
command1_set = set(command1[-1].split(','))
command2_set = set(command2[-1].split(','))

i = 2
command_intersec = list(command1_set.intersection(command2_set))
command_intersec_int = [int(i) for i in command_intersec]
command_intersec_int.sort()
print (command_intersec_int)


