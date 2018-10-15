#!/usr/bin/python

import dev
import mydevices
import datetime
import time

starttime = time.time()
ts = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H_%M_%S')

core = mydevices.devices[0]
devices = mydevices.devices

dev.printdevs(devices)

#dev.printdev(devices)

ts=datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H_%M_%S')
print ts
print "\n Done running "+str(len(shows))+" Commands in " + str( time.time() - starttime)
