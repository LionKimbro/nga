#!/usr/bin/env python3

import os

def extract_from_markdown(name):
    v = []
    with open(name) as f:
        v = f.readlines()
    s = []
    fence = False
    for l in v:
        l = l.rstrip()
        if fence == True and l != '````':
            s.append(l)
        elif l == '````' and fence == True:
            fence = False
        elif l == '````' and fence == False:
            fence = True
    return s


def convert(s, d):
    with open(d, 'w') as file:
        lines = extract_from_markdown(s)
        for line in lines:
            file.write(line)
            file.write('\n')

if __name__ == '__main__':
    convert('Nga_C.md', 'bin/nga.c')
    convert('Nga_Python.md', 'bin/nga.py')
    convert('Naje.md', 'bin/naje.py')
    convert('Nabk.md', 'bin/nabk.py')
