#!/usr/bin/python

import dev
import mydevices
import datetime

core = mydevices.devices[0]
devices = mydevices.devices

dev.printdevs(devices)

#dev.printdev(devices)

ts=datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H_%M_%S')
print ts