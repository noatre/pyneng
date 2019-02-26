#!/usr/bin/env python3

from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']

file = argv[1]
with open(file, 'r') as f, open('config_sw1_cleared.txt', 'w') as f_out:
    for line in f:
        a = 0
        for ign in ignore:
            if line.count(ign) > 0:
                a += 1
        if a == 0:
            f_out.write(line)

