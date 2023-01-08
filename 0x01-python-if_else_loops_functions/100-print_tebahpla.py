#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    if i % 2 == 0:
        dif = 0
    else:
        dif = 32
    print('{}'.format(chr(i - dif)), end='')
