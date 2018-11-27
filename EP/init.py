#!/usr/bin/python

import dev
import mydevices
import config
import connect
import show_commands
import scenario
import datetime
import time
import os
from os import listdir
from os.path import isfile, join

#starttime = time.time()
#ts = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H_%M_%S')

#core = mydevices.devices[0]
devices = mydevices.devices
mypath='templates/'

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


'''Menu '''
while True:
    cls()
    print" 1.  Device List \n 2.  Devices Menu\n 3.  Config Menu \n 4.  Scenarios \n 10. Pull info from device \n e.  Exit"
    input=raw_input("Select: ")
    if input == '1':
        dev.printdevs(devices)
        print "\nYou have " + str(len(devices)) + " devices total."
        raw_input("\nPress any key..")
    elif input == '2':
        while True:
            print " 1. Add device \n 2. Edit Device \n e. Back"
            device_input = raw_input("Select: ")
            if device_input == '1':
                dev.adddev(devices)
                print "You have " + str(len(devices)) + " devices total."
                raw_input("\nPress any key..")
                break
            elif device_input =='2':
                num=raw_input("Enter device ID to edit")
                if num.isdigit() == True and int(num) < len(devices):
                    dev.editdev(devices,num)
                break
            elif device_input == 'e':
                break
    elif input =='3':
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

        for files in onlyfiles:
            print str(onlyfiles.index(files))+"." +files

        while True:
            file_name= raw_input("Select: ")
            if file_name.isdigit() == True:
                if int(file_name) <= onlyfiles.index(files):
                    file_name = onlyfiles[int(file_name)]
                    break
        cls()
        print "Loading "+ file_name +" Template\n"
        path = mypath+file_name
        device_config = config.load_config(path,0)
        while True:
            savetofile= raw_input("Save to file? [Y/N]")
            if savetofile.capitalize()=='Y':
                filename = raw_input("Enter filename:")
                config.writetofile(device_config,filename)
                break
            if savetofile.capitalize()=='N':
                for line in device_config:
                    print line
                raw_input("Press any key to continue..")
                break

        while True:
            if raw_input("Provision configs to device? [Y/N]").capitalize() == 'Y':
                dev.printdevs(devices)
                output=connect.devcon(device_config,devices,raw_input("Select device:"),'config')
                raw_input(("Press any key to see output.."))
                for command in output:
                    for line in command:
                        print line
                raw_input("Press any key to continue..")
                break
            elif raw_input("Provision configs to device? [Y/N]").capitalize() == 'N':
                raw_input("Press any key to continue..")
                break
        raw_input("\nPress and key..")
    elif input =='4':
        scenrio_menu=raw_input("1. IPSec WAN link\n2. MACSec WAN link")
        if scenrio_menu.isdigit() and scenrio_menu=='1':
            scenario.ipsec()
        elif scenrio_menu.isdigit() and scenrio_menu =='2':
            print "MACSEEEECCC"

        raw_input("\nPress any key..")
    elif input == '10':
        shows = show_commands.show_menu()
        dev.printdevs(devices)
        output=connect.devcon(shows, devices, raw_input("Select device:"),'show')

        while True:
            savetofile= raw_input("Save to file? [Y/N]")
            if savetofile.capitalize()=='Y':
                filename = raw_input("Enter filename:")
                connect.writetofile(output,filename)
                raw_input("Press any key to continue..")
                break
            if savetofile.capitalize()=='N':
                for command in output:
                    for line in command:
                        print line
                raw_input("Press any key to continue..")
                break

    elif input== 'e':
        break

#dev.printdev(devices)


## Calculate runtime ###
# ts=datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H_%M_%S')
# print ts
# print "\n Done running  Commands in " + str( time.time() - starttime)
