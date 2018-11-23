
def ipsec():
    devices = [
        {
            'mode': 'NAT',
            'int': ' ',
            'ip': '1.1.1.1'
        },

        {
            'mode': 'NAT',
            'int': ' ',
            'ip': '1.1.1.2/30'
        },
    ]
    side_a=devices[0]
    side_b=devices[1]
    #print '-'*20+'\n'+'| '+ ' '*1+'ipsec'
    print "Side A"+' '*40+"Side B"
    print "Mode: "+side_a['mode'] + ' '*15 + "Mode: "+side_b['mode']
    print "WAN Interface["+side_a['int']+']' + ' '*15+'WAN Interface['+side_b['int']+']'
    print "WAN IP["+side_a['ip']+']' + ' '*15+'WAN IP['+side_b['ip']+']'