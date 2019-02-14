#!/usr/bin/env python3

MAC = 'AAAA:BBBB:CCCC'

MAC = MAC.split(':')
MAC = ''.join(MAC)
print(bin(int(MAC, 16)))
