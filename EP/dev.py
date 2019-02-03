import re
# print core['name'] +" " + core['ip']

# core['ip'] = "10.56.100."+str(2)

# print core['ip']
#s
# ######  -l list #########
def devlist(device,num):
    print "\nDevice #" + str(num) + ":"
    print "Hostname:     "+ device['name']
    print "IPv4 address: " + device['ip']
    print "Port:         " + device['port']
    print "Username:     " + device['username']
    print "Password:     " + device['password']
    print "Enable:       " + device['enable']
    #for arg in device:
     #   print arg + ':  ' + device[arg]
      #  print device.index(arg)

def printdevs(devices):
    print "\n\n  Device List\n  -----------"
    for device in devices:
        devlist(device,devices.index(device))


# core['ip']= raw_input("Please Change IP:")

# print core['ip'].split(".")
# print type(core['ip'].split("."))


def adddev(mydevices):
    mydevices.append({'name' : ' ','ip' : '','username' : '','password' : '','enable' : '','port' :  '',})
    dev=mydevices[-1]
    dev['name'] = raw_input("Please enter the hostname:")

    while True:
        dev['ip'] = raw_input("Enter Management IPv4 address: ")
        if re.match(r'^((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])\.){3}(\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])$', dev['ip']):
            break
        else:
            print "Invalid IP"

    while True:
        dev['port'] = raw_input("Please enter port number [23]: ") or '23'
        if dev['port'].isdigit() and int(dev['port']) < 65535:
            break
    dev['username']=raw_input("Username: ")
    dev['password'] = raw_input("Password: ")
    dev['enable']=raw_input("Enable Password: ")
    devlist(dev, len(mydevices)-1)

def editdev(mydevices,num):
    dev=mydevices[int(num)]
    dev['name'] = raw_input("Please enter the hostname[" +dev['name']+ "]:") or dev['name']

    while True:
        dev['ip'] = raw_input("Enter Management IPv4 address[" +dev['ip']+ "]:") or dev['ip']
        if re.match(r'^((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])\.){3}(\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])$', dev['ip']):
            break
        else:
            print "Invalid IP"
    while True:
        dev['port'] = raw_input("Please enter port number [" +dev['port']+ "]:") or dev['port']
        if dev['port'].isdigit() and int(dev['port']) < 65532:
            break
    dev['username']=raw_input("Username [" +dev['username']+ "]:") or dev['username']
    dev['password'] = raw_input("Password [" +dev['password']+ "]:") or dev['password']
    dev['enable']=raw_input("Enable Password [" +dev['enable']+ "]:") or dev['enable']
    devlist (dev,int(num))