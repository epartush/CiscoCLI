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
import re

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
    print "\n ##### ZING #####"
    print" 1.  Devices Menu\n 2.  Config Templates \n 3.  WAN Builder \n 10. Pull info \n q.  Quit"
    input=raw_input("\nSelect: ")

    if input == '1':
        while True:
            cls()
            print "\n ##### Devices #####\n 1.  Device list \n 2.  Edit Device \n 3.  Add device\n b.  Back"
            device_input = raw_input("Select: ")
            if device_input == '3':
                dev.adddev(devices)
                print "You have " + str(len(devices)) + " devices total."
                raw_input("\nPress any key..")
                break
            elif device_input =='2':
                dev.printdevs(devices)
                num=raw_input("Enter device ID to edit[0-"+str(len(devices)-1)+ "]: ")
                if num.isdigit() == True and int(num) < len(devices):
                    dev.editdev(devices,num)
                    break
            elif device_input == 'b':
                break
            elif device_input == '1':
                dev.printdevs(devices)
                print "\nYou have " + str(len(devices)) + " devices total."
                raw_input("\nPress any key..")

    elif input =='2':
        # print files
        while True:
            cls()

            file_name = config.list_template(mypath)
            if file_name == 'b':
                break
            print "Loading "+ file_name +" Template\n"
            path = mypath+file_name
            device_config = config.load_config(path,0)
            raw_input("..........")
        # print template

        # rebuilld
            build = raw_input("Press 'y' to build config from template.")
            if build.lower() == 'y':
                config.rebuild(0,device_config)
            raw_input("....... ......")
        # save to file





        '''while True:
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
            else:
                break
            '''
    elif input =='3':
        while True:
            cls()
            scenrio_menu=raw_input("\n ##### Builder #####\n 1.  IPSec WAN link\n 2.  MACSec WAN link\n b.  Back\n\n Please enter your choice..")
            if scenrio_menu.isdigit() and scenrio_menu=='1':
                scenario.wan(devices,"ipsec")
            elif scenrio_menu.isdigit() and scenrio_menu =='2':
                scenario.wan(devices,"macsec")
            elif scenrio_menu.lower() == 'b':
                break

        #raw_input("\nPress any key..")
    elif input == '10':
        shows = show_commands.show_menu()
        if len(shows) != 0:

            dev.printdevs(devices)
            output=connect.devcon(shows, devices, raw_input("Select device:"),'show')

            if output != 'none':

                while True:
                    savetofile= raw_input("Save to file? [Y/N]")
                    if savetofile.capitalize()=='Y':
                        filename = raw_input("Enter filename:")
                        connect.writetofile(output,filename)
                        #raw_input("Press any key to continue..")
                        break
                    if savetofile.capitalize()=='N':
                        for command in output:
                            for line in command:
                                print line
                        #raw_input("Press any key to continue..")
                        break
            raw_input("Press any key to continue..")
    elif input== 'q':
        break
    elif input == 't':

        while True:
            ip = raw_input("Enter IP address:")
            '''if len(ip.split(".")) == 4:
                ip = ip.split(".")
                if ip[0].isdigit() and int(ip[0])>0 and int(ip[0])<224 and ip[1].isdigit() and int(ip[1]) >= 0 and int(ip[1])<256:
                    if ip[2].isdigit() and int(ip[2])>= 0 and int(ip[2])<256:
                        if ip[3].isdigit() and int(ip[3])>=0 and int(ip[3]) < 255:
                            break
        
        ip=".".join(ip)'''
            if re.match(r'^((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])\.){3}(\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])$', ip):
                print "Valid IP"
                break
            else:
                print "Invalid IP"
        print ip
        print type(ip)
        #dev.printdev(devices)


## Calculate runtime ###
# ts=datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H_%M_%S')
# print ts
# print "\n Done running  Commands in " + str( time.time() - starttime)
