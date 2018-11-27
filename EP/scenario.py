import config
def ipsec():
    devices = [
        {
            'int': 'gi0/1',
            'ip': '10.0.0.1',
            'mode': 'NAT',
        },

        {

            'int': ' ',
            'ip': '101.1.2.3',
            'mode': 'Static',
        },
    ]
    side_a=devices[0]
    side_b=devices[1]
    spaces = 50
    table=['WAN Interface: ','WAN IP[IP/DHCP]: ','Mode[NAT/P2P]: ']
    print "Side A"+' '*int(spaces-len('Side A')) +"Side B"+'\n'+'------'+' '*int(spaces-len('Side A'))+'------'

    index=0
    for value in side_a:
        print table[index] + side_a[value] + ' '*int(spaces-len(side_a[value])-len(table[index])) + table[index]+side_b[value]
        index += 1
    side_a['dest']=side_b['ip']
    side_a['tunnel']='10.10.10.1'
    side_b['dest']=side_a['ip']
    side_b['tunnel']='10.10.10.2'
    raw_input("press any key..")
    if side_a['mode'] == 'NAT':
        side_a_conf = config.load_config('templates/IPSecOverNat',side_a)

    if side_b['mode'] == 'Static':
        side_b_conf = config.load_config('templates/IPSec',side_b)

    for a,b in zip(side_a_conf,side_b_conf):
        if len(side_a_conf) > len(side_b_conf):
            print a + ' '*(50-int(len(a))) + b
        else:
            print b + ' '*(50-int(len(b))) + a
    raw_input("press any key..")