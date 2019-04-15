#!/usr/bin/python

import os
import sys
import config

template_path='templates/'

if len(sys.argv) <= 1:
    print "Use -T for text only.  -G for GUI . -C for curses menu"
    sys.exit(0)
arguments={}
mode = sys.argv[1]
if mode[-1:].lower() == 't':
    print "Text Mode"
    if len(sys.argv) < 3:
        print "format -T <name of template> <interface> <ip> <tunnelip> <ip> <f> <g>"
        sys.exit(0)
    elif len(sys.argv) >= 6:
        #arguments.append(sys.argv[2])
        arguments['int']=(sys.argv[3])
        arguments['ip']=(sys.argv[4])
        arguments['tunnel']=(sys.argv[5])
        #arguments.append(sys.argv[6])
        #arguments.append(sys.argv[7])
        newconf = config.load_config((template_path+sys.argv[2]) , arguments)

    for line in newconf:
        print line

elif mode[-1:].lower() == 'c':
    print "Curses Mode"
    import init.py
elif mode[-1:].lower() == 'g':
    print "GUI Mode"




