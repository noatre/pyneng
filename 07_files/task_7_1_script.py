#!/usr/bin/env python3

template = ('''
Protocol:              {}
Prefix:                {}
AD/Metric:             {}
Next-Hop:              {}
Last update:           {}
Outbound Interface:    {}
''')
f = open('ospf.txt', 'r')

for str in f:
    str_list_clean = []
    str = str.rstrip('\n')
    str = str.split()
    for i in str:
        i = i.strip('[],')
        if i == 'O':
            str_list_clean.append('OSPF')
        elif i == 'via':
            pass
        else:
            str_list_clean.append(i)
    print(template.format(*str_list_clean))

f.close()
