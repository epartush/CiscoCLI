import socket
import sys,os
import time
import datetime
from os import path



def devcon(show_commands,devices,device):
    def sendc(command, timer):
        if timer == ' ':
            timer = 0.2
        print "!! " +command+ " !!"
        s.send(command + '\r')
        time.sleep(timer)
        output.append(s.recv(65535).split('\r\n'))


    dev = devices[int(device)]
    output=[]

    print "THIS IS DEVCON Function"
    #print "connecting to "+ dev['ip'] +" "+dev['name']
    print "using " +dev['username']+ ' as username and ' + dev['password'] + ' as password '

    '''for line in config:
        #print "pushing-> " + line
        print str(config.index(line)+1) + " out of " + str(len(config))
        sys.stdout.flush()
        time.sleep(0.3)
'''

    print "connecting to " + dev['ip'] + " " + dev['port'] + " " + dev['name']
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port= int(dev['port'])
    s.connect((dev['ip'], port))
    time.sleep(1)
    output.append(s.recv(512).rstrip().split('\r\n'))
    if output[-1][-1][1:]== 'sername:':
        print "this is awsome!!"
        sendc(dev['username'], ' ')
        sendc(dev['password'], ' ')

        print "I'm in! \n"
        prompt = output[-1][-1]
        print "Prompt is " + prompt + '\n'
        if prompt[-1] == '#':
            print "No need for escalation, let's go to work\n"
        elif prompt[-1] == '>':
            print "Enabling with " + dev['enable']
            s.send('enable\r')
            s.send(dev['enable']+ '\r')
    #print s.recv(1024)
    else:
        print "what tha?"
    #output.append(s.recv(1024).split('\r\n'))

    #sendc('ter len 0', ' ')
    #sendc('show run',5)
    #sendc('show ip protocols',' ')
    for show in show_commands:
        if show == 'show run':
            print "\n\n\nBingo!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\n"
            sendc(show,5)
        else:
            sendc(show, ' ')


    s.close()


    for command in output:
        for line in command:
            print line


def TBD():


   #'''creates directory ig not exists'''

    os.mkdir(path, 0755)
    if not os.path.exists(ips):
        os.mkdir(ips, 0755)


    # Create a Socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the Server 'IP' and Port
    # s.connect(('10.56.100.1',23))
    print "Connecting to "+ips+":"+ str(port)
    s.connect((ips,port))


    for command in login:
        s.send (command + '\n')
        time.sleep(0.3)

    f = open(path+'/'+ips+"_"+"login"+".txt",'w+')
    data = s.recv(1024)
    f.write(data)
    print "####Login complete###\n"


    print ts



    s.recv(0)

    #print "DATA =" + data  + '\n'

    for command in shows:
        print 'Running '+command+".."
        # f = open(path+'/'+ips+"_"+"_".join(command.split())+".txt",'wr')
        # f.write(command)
        fi = open(ips+'/'+"_".join(command.split())+"_"+path+".txt",'w+')
        fi.write("########" +command+"##########\n" )
        s.send (command + '\n')
        time.sleep(0.3)
        data = s.recv(65536)
        time.sleep(0.3)
        #print data
        # f.write(data)
        fi.write(data)
        #f.close()
        fi.close()
        print "Done.\n"
        time.sleep(0.3)
        s.recv(0)
    print prompt
