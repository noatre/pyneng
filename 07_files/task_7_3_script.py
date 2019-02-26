#!/usr/bin/env python3

with open('CAM_table.txt') as f:
    for line in f:
        if line.count('Gi') == 1:
            line = line.replace('DYNAMIC', '')
            print(line)
