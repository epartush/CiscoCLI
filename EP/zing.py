#!/usr/bin/python

import os
import sys
import config
import init
from os import listdir
from os.path import isfile, join

template_path='./templates/'
arguments={}

def loadc(template):
    print template
    f = open(template , 'r').readlines()
    for line in f:
        line = line.strip('\n').split(" ")
        for word in line:
            if word != '':
                if word[0] == '%':
                    arguments[word[1:]] =[]

    return arguments



if len(sys.argv) == 1:
    print"""Usage:
        -t: Text Mode
        -g: GUI Mode
        -c: Curses menu"""


elif len(sys.argv) >= 2:
    mode = sys.argv[1].lower()

    if mode == '-t':
        print "Text Mode"

        onlyfiles = [f for f in listdir(template_path) if isfile(join(template_path, f))]
        if len(sys.argv) > 2:
            tem = sys.argv[2]
            if tem == '-h':
                print "help"
            if tem in onlyfiles:
                print tem
                arguments = loadc(template_path+tem)
            else:
                print "No such template"
            if len(sys.argv) == 3:
                print "Use the argument: "+ tem + " " + " ".join([key + " <value> " for key in arguments])

            if len(sys.argv) > 3:
                arg_num = len(sys.argv)-1
                if (len(sys.argv)-3) == len(arguments)*2:
                    for i in range(3,arg_num,2):
                        arguments[sys.argv[i]] = sys.argv[i+1]

                    print arguments
                    newconf  = config.load_config(template_path+tem,arguments)
                    print "".join([line + '\n' for line in newconf])
                else:
                    print "Use the argument: "+ tem + " " + " ".join([key + " <value>" for key in arguments])
        if len (sys.argv) == 2:
            print "Templates available:"
            print ", ".join([file for file in onlyfiles])


    elif mode == '-c':
        print "Curses Mode"
        init.curses()

    elif mode == '-g':
        print "GUI Mode"

    else:
        print """Usage:
        -t: Text Mode
        -g: GUI Mode
        -c: Curses menu"""
        sys.exit(0)




