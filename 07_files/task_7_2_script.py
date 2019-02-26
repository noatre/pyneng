#!/usr/bin/env python3

from sys import argv
file = argv[1]
with open(file, 'r') as f:
    for line in f:
        print(line.rstrip('\n').lstrip('!'))

