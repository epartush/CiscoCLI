
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
    spaces = 50
    table=['Mode: ','WAN Interface: ','WAN IP: ']

    print "Side A"+' '*int(spaces-len('Side A')) +"Side B"+'\n'+'------'+' '*int(spaces-len('Side A'))+'------'
    print table[0]+side_a['mode'] + ' '*int(spaces-len(side_a['mode'])-len(table[0]))+table[0]+side_b['mode']
    print table[1]+side_a['int'] + ' '*int(spaces-len(side_a['int'])-len(table[1]))+table[1]+side_b['int']
    print table[2]+side_a['ip'] + ' '*int(spaces-len(table[2])-len(side_a['ip']))+table[2]+side_b['ip']

    #for line in table:
    #    print line+side_a[]