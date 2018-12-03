import config

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
            'mode': 'Static',
            'role': 'Spoke'
        },
    ]
    side_a=devices[0]
    side_b=devices[1]
    spaces = 50
    table=['WAN Interface: ','WAN IP[IP/DHCP]: ','Mode[NAT/Public/P2P]: ','Role[Hub/Spoke]:']

    while True:
        print "Side A"+' '*int(spaces-len('Side A')) +"Side B"+'\n'+'------'+' '*int(spaces-len('Side A'))+'------'
        index=0
        for value in sorted(side_a):
            print table[index] + side_a[value] + ' '*int(spaces-len(side_a[value])-len(table[index])) + table[index]+side_b[value]
            index += 1
        if raw_input("press any key to change or e for execute..") == 'e'.lower():
            break


    side_a['dest']=side_b['ip']
    side_a['tunnel']='10.10.10.1'
    side_b['dest']=side_a['ip']
    side_b['tunnel']='10.10.10.2'


    if side_a['mode'] == 'NAT':
        side_a_conf = config.load_config('templates/IPSecOverNat',side_a)

    if side_b['mode'] == 'Static':
        side_b_conf = config.load_config('templates/IPSec',side_b)

    if len(side_a_conf) > len(side_b_conf):
        for i in range(0,len(side_a_conf)-len(side_b_conf),1):
            side_b_conf.append("!")
    else:
        for i in range(0,len(side_b_conf)-len(side_a_conf),1):
            side_a_conf.append("!")


    for a,b in zip(side_a_conf,side_b_conf):
        print a + ' '*(50-int(len(a))) + b
    raw_input("press any key..")