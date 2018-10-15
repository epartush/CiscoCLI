
# print core['name'] +" " + core['ip']

# core['ip'] = "10.56.100."+str(2)

# print core['ip']

# ######  -l list #########
def devlist(device):
    print ("---" + device['name'] + "---")
    for arg in device:
        print arg + ':' + device[arg]


def printdevs(devices):
    print "\n\n ###printing Device List now ###"
    for device in devices:
        devlist(device)


# core['ip']= raw_input("Please Change IP:")

# print core['ip'].split(".")
# print type(core['ip'].split("."))

def printdev(mydevices):
    core = mydevices[0]
    inputok =0
    while inputok != 4:
        inputok = 0
        countchar = 0
        core['ip'] = raw_input("enter IP: ")

        if len(core['ip'].split(".")) == 4:
            for octet in core['ip'].split("."):
                if octet != '' and int(octet) > 0 and int(octet) <= 255:
                    inputok +=1
                else:
                    print str(octet) + " is not a number between 1 - 255"
                    inputok = 0
                    break
        else:
            print "Use IPv4 Address format: x.x.x.x"


    while 1:
        core['port'] = raw_input("Please enter port number -[23]:") or '23'
        if core['port'].isdigit() == True and int(core['port'])<65532:
            break

    print core