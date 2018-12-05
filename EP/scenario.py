import config
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def ipsec():

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
    side_b=devices[1]
    spaces = 50
    table=['WAN Interface: ','IP Address[IP/DHCP]: ','Mode[NAT/Public/P2P]: ','Role[Hub/Spoke]:']

    while True:
        cls()
        print "Side A"+' '*int(spaces-len('Side A')) +"Side B"+'\n'+'------'+' '*int(spaces-len('Side A'))+'------'
        print table[0] + side_a['int'] + ' '*int(spaces-len(side_a['int'])-len(table[0])) + table[0]+side_b['int']
        print table[1] + side_a['ip'] + ' '*int(spaces-len(side_a['ip'])-len(table[1])) + table[1]+side_b['ip']
        print table[2] + side_a['mode'] + ' '*int(spaces-len(side_a['mode'])-len(table[2])) + table[2]+side_b['mode']
        print table[3] + side_a['role'] + ' '*int(spaces-len(side_a['role'])-len(table[3])) + table[3]+side_b['role']
        input = raw_input("\nPress C for change or E for execute or B for back..")
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
                    execute(side_a,side_b)
                    break
        elif input.lower() == 'c':
            while True:
                num = raw_input("Select Device:[0-1]")
                if num == '0' or num =='1':
                    editdev(devices,num)
                    break
                elif num == 'b':
                    break
        elif input.lower() == 'b':
            break


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
