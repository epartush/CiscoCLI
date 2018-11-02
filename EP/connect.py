import socket
import sys,os
import time
import datetime
from os import path

def devcon(config,devices,device):
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
    output.append(s.recv(512).split('\r\n'))
    print output[-1][-1][1:]
    #s.recv(0)
    if output[-1][-1][1:]== 'sername: ':
        print "this is awsome!!"
        s.send(dev['username'] + '\r\n')
        time.sleep(0.2)
        output.append(s.recv(100).split('\r\n'))
        s.send(dev['password'] + '\r\n')
        time.sleep(0.2)
        output.append(s.recv(100).split('\r\n'))
    #print s.recv(1024)
    else:
        print "what tha?"
    #output.append(s.recv(1024).split('\r\n'))
    s.send('ter len 0 \r\n')
    time.sleep(0.3)
    s.send('show run \r\n')
    time.sleep(0.3)
    output.append(s.recv(65535).split('\r\n'))
    prompt = output[-1][-1]
    print "Prompt is " + prompt +'\n'
    s.close()

    for command in output:
        for line in command:
            print line


def TBD():
    # shows=['show clock']
    shows=["show running","show ip int br","show ip route", "show ip protocols", "show clock","show platform", "show module", "show version", "show cdp ne", "show inventory | i PID"]
    # login=["lions", "lions", "enable 15", "bonanza1947", "ter len 0"]
    login=["ter len 0"]

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

    data = s.recv(0)
    prompt = " "
    s.send ('\n')
    s.send ('\n')
    time.sleep(0.5)
    prompt = s.recv(12)
    print prompt
    s.send ('\n')
    #time.sleep(0.5)
    #data = s.recv(8192)
    #print data
    #data = s.recv (0)
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
