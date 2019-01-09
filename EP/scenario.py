import config
import os,socket
import time


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#conn
def check_connection(host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    port = int(host['port'])
    try:
        s.connect((host['ip'],port))
        #time.sleep(1)
        s.close()
        return ('\x1b[6;30;42m' + 'ZING!' + '\x1b[0m')
    except socket.error , exc:
        s.close()
        return ('\x1b[1;31;40m'+ str(exc) +'\x1b[0m')


def ipsec(devices_connect):

    devices = [
        {
            'int': 'gi0/1',
            'ip': '10.0.0.1',
            'mode': 'NAT',
            'role': 'Spoke'
        },

        {

            'int': ' ',
            'ip': '101.1.2.3',
            'mode': 'P2P',
            'role': 'Spoke'
        },
    ]
    side_a=devices[0]
    side_a_connect=devices_connect[0]
    side_b=devices[1]
    side_b_connect=devices_connect[1]
    spaces = 50
    table=['WAN Interface: ','IP Address[IP/DHCP]: ','Mode[NAT/Public/P2P]: ','Role[Hub/Spoke]:']


    while True:
        cls()
        print "Side A"+' '*int(spaces-len('Side A')) +"Side B"+'\n'+'------'+' '*int(spaces-len('Side A'))+'------'
        print table[0] + side_a['int'] + ' '*int(spaces-len(side_a['int'])-len(table[0])) + table[0]+side_b['int']
        print table[1] + side_a['ip'] + ' '*int(spaces-len(side_a['ip'])-len(table[1])) + table[1]+side_b['ip']
        print table[2] + side_a['mode'] + ' '*int(spaces-len(side_a['mode'])-len(table[2])) + table[2]+side_b['mode']
        print table[3] + side_a['role'] + ' '*int(spaces-len(side_a['role'])-len(table[3])) + table[3]+side_b['role']


        print '='*30 +"CONNECTION DETAILS" + '='*30
        print "Mgmt IP:" + side_a_connect['ip'] + ' '* int(spaces-len(side_a_connect['ip'])-len('Mgmt IP:'))+ "Mgmt IP:"+side_b_connect['ip']
        print "Status: " + check_connection(side_a_connect) + ' '* 37 + "Status: " + check_connection(side_b_connect)




        input = raw_input("\nPress M to Modify\nPress E to execute\nPress B to go back\n  Please enter your selection: ")
        if input.lower() == 'e':
            while True:
                value =0
                for device in devices:
                    for key in device:
                        if device[key] == ' ':
                            raw_input("All values should be entered before execution!")
                            value=1

                if value==1:
                    break
                else:
                    side_a_config,side_b_config=execute(side_a,side_b)
                    while True:
                        savetofile= raw_input("Save to file? [Y/N]")
                        if savetofile.capitalize()=='Y':
                            filenamea = raw_input("Enter filename for SideA:")
                            filenameb = raw_input("Enter filename for SideB:")
                            config.writetofile(side_a_config,filenamea)
                            config.writetofile(side_b_config,filenameb)
                            break

                        raw_input("Press any key to continue..")
                        break
                    break
        elif input.lower() == 'm':
            while True:
                num = raw_input("Select Device:[A/B]")

                if num == 'a':
                    editdev(devices,'0')
                    break
                elif num.lower() == 'b':
                    editdev(devices,'1')
                    break
                elif num == 'e':
                    break
        elif input.lower() == 'b':
            break




'''while True:
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
        break'''
#s
def execute(side_a,side_b):
    side_a['dest']=side_b['ip']
    side_a['tunnel']='10.10.10.1'
    side_b['dest']=side_a['ip']
    side_b['tunnel']='10.10.10.2'
    side_a_conf=[]
    side_b_conf=[]
    if side_a['mode'].lower() == 'nat':
        side_a_conf = config.load_config('templates/IPSecOverNat',side_a)
    elif side_a['mode'].lower() == 'p2p':
        side_a_conf = config.load_config('templates/IPSecOverNat',side_a)
    elif side_a['mode'].lower() == 'public':
        side_a_conf = config.load_config('templates/IPSecOverNat',side_a)

    if side_b['mode'].lower() == 'p2p':
        side_b_conf = config.load_config('templates/IPSec',side_b)
    elif side_b['mode'].lower() == 'nat':
        side_b_conf = config.load_config('templates/IPSecOverNat',side_b)
    elif side_a['mode'].lower() == 'public':
        side_b_conf = config.load_config('templates/IPSecOverNat',side_b)

    if len(side_a_conf) > len(side_b_conf):
        for i in range(0,len(side_a_conf)-len(side_b_conf),1):
            side_b_conf.append("!")
    else:
        for i in range(0,len(side_b_conf)-len(side_a_conf),1):
            side_a_conf.append("!")


    for a,b in zip(side_a_conf,side_b_conf):
        print a + ' '*(50-int(len(a))) + b
    return side_a_conf,side_b_conf
    raw_input("press any key..")


def editdev(mydevices,num):
    dev=mydevices[int(num)]
    inputok = 0
    #dev['name'] = raw_input("Please enter the hostname[" +dev['name']+ "]:") or dev['name']
    dev['int']=raw_input("WAN Interface [" +dev['int']+ "]:") or dev['int']
    #dev['ip'] = raw_input("Enter IPv4 for WAN Interface[" +dev['ip']+ "]:") or dev['ip']
    while inputok != 4:
        inputok = 0
        dev['ip'] = raw_input("Enter IPv4 for WAN Interface["+dev['ip']+"]:") or dev['ip']

        if len(dev['ip'].split(".")) == 4:
        #print dev['ip'].split(".")
            for octet in dev['ip'].split("."):
                if octet.isdigit() == True:
                    if octet != '' and int(octet) >= 0 and int(octet) <= 255:
                        inputok += 1
                    else:
                        print str(octet) + " is not a number between 1 - 255"
                        inputok = 0
                        break
                else:
                    print "Numbers only"
        else:
            print "Use IPv4 Address format: x.x.x.x"

    #while 1:
    #    dev['port'] = raw_input("Please enter port number [" +dev['port']+ "]:") or dev['port']
    #    if dev['port'].isdigit() == True and int(dev['port']) < 65532:
    #        break

    while True:
        dev['mode'] = raw_input("Mode- Behind NAT, Public, P2P [" +dev['mode']+ "]:") or dev['mode']
        if dev['mode'].lower() == 'p2p' or dev['mode'].lower() == 'nat' or dev['mode'].lower() == 'public':
            break
    dev['role']=raw_input("Role Hub or Spoke [" +dev['role']+ "]:") or dev['role']
