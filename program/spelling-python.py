#!/usr/bin/python
import os
import sys

if len(sys.argv) == 1:
    arg = 'Please supply any word in English, and I will spell it for you'
    spell = None
else:
    arg = sys.argv[1]
    spell = ''
    prev = None
    for a in arg:
        if prev == a:
            spell = spell[:-2] + ' double ' + a + ','
        else:
            spell = spell + a + ','
        prev = a

os.system('say ' + arg)
if spell is not None:
    #print spell
    os.system('say ' + spell)
