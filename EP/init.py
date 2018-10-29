#!/usr/bin/python

import dev
import mydevices
import config
import datetime
import time
from os import listdir
from os.path import isfile, join

#starttime = time.time()
#ts = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H_%M_%S')

#core = mydevices.devices[0]
devices = mydevices.devices
mypath='templates/'



'''Menu '''
while True:
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
    elif input =='4':
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

        for files in onlyfiles:
            print str(onlyfiles.index(files))+"." +files

        while True:
            file_name= raw_input("Select: ")
            if file_name.isdigit() == True:
                if int(file_name) <= onlyfiles.index(files):
                    file_name = onlyfiles[int(file_name)]
                    break

        print "Loading"+ file_name +" Template\n"
        path = mypath+file_name
        default_config = config.load_config(path)
        while True:
            savetofile= raw_input("Save to file? [Y/N]")
            if savetofile.capitalize()=='Y':
                filename = raw_input("Enter filename:")
                config.writetofile(default_config,filename)
                break
            if savetofile.capitalize()=='N':
                for line in default_config:
                    print line
                break


        raw_input("\nPress any key..")

    elif input== 'e':
        break

#dev.printdev(devices)


## Calculate runtime ###
# ts=datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H_%M_%S')
# print ts
# print "\n Done running  Commands in " + str( time.time() - starttime)
