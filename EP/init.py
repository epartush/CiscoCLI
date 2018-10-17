#!/usr/bin/python

import dev
import mydevices
import datetime
import time

#starttime = time.time()
#ts = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H_%M_%S')

#core = mydevices.devices[0]
devices = mydevices.devices
input = '0'


while input != 'e':
    print" 1. Add Device \n 2. List the devices \n 3. Store log \n 4. Config Menu \n 5. Edit device\n e. Exit"
    input=raw_input("Select: ")
    if input == '2':
        dev.printdevs(devices)
        print "\nYou have " + str(len(devices)) + " devices total."
        raw_input("\nPress any key..")
    elif input == '1':
        dev.adddev(devices)
        print "You have " + str(len(devices)) + " devices total."
        raw_input("\nPress any key..")
    elif input =='5':
        num=raw_input("Enter device ID to edit")
        if num.isdigit() == True and int(num) < len(devices):
            dev.editdev(devices,num)

#dev.printdev(devices)


## Calculate runtime ###
# ts=datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H_%M_%S')
# print ts
# print "\n Done running  Commands in " + str( time.time() - starttime)
