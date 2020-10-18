#!/usr/bin/python
# https://github.com/ilturbo

import re

def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)
 
def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m
 


with open("List.txt", "r") as fr, open("Save.txt", "a") as fw:
    for line in fr:
        N = 0xD485E1AC
        A = 0xE7CD263B
        L = int(line, 0)
#       val = str(hex((A * num)))
        val = str(hex(L * A) % N)
        if len(val) < 66:
            vals = val.split('x')
            vals.insert(1, 'x' + '0' * (66 - len(val)))
            val = ''.join(vals)
        print(val, file=fw)
