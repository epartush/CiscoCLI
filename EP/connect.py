import socket
import sys,os
import time
import datetime
from os import path
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def devcon(commands,devices,device,isconf):
    def sendc(command, timer):
        if timer == ' ':
            timer = 0.3
        #print "!! " +command+ " !!"
        s.send(command + '\r')
        time.sleep(timer)
        output.append(s.recv(65535).split('\r\n'))

    while True:
        if device.isdigit() and int(device) < len(devices):
            dev = devices[int(device)]
            break
        else:
            device=raw_input("Select Device [0-" +str(len(devices)-1) + "]: ")
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
    output.append(s.recv(1024).rstrip().split('\r\n'))
    #print "output" + str(output)
    #print output[-1][-1][1:]
    if output[-1][-1][1:]== 'sername:':
        #print "this is awsome!!"
        sendc(dev['username'], ' ')
        sendc(dev['password'], ' ')

        print "Login Succesful  \n"
        prompt = output[-1][-1]
        print "Prompt is " + prompt + '\n'
        if prompt[-1] == '#':
            print "No need for escalation, let's go to work\n"
        elif prompt[-1] == '>':
            print "Enabling with " + dev['enable']
            s.send('enable\r')
            s.send(dev['enable']+ '\r')
    #print s.recv(1024)
        sendc('ter len 0', ' ')
    else:
        print "what tha?"
    if isconf=='config':
        print "conf t\n"
        sendc('conf t', ' ')
        for command in commands:
            print command
            sendc(command, ' ')
        sendc('end', ' ')
    else:

        astrix=0
        for show in commands:
            cls()
            astrix+=1
            print '#'*astrix + '_'*int(len(commands)-astrix)
            if show == 'show running':
                print "\n\n5 Seconds.. \n\n"
                sendc(show,5)
            else:
                sendc(show, ' ')


    s.close()


    #print output
    return output


def writetofile (output,filename):
    import time
    from datetime import datetime
    TS = datetime.fromtimestamp(time.time()).strftime('%H-%M-%S')
    f = open ('show_output/'+filename+TS+'.txt', 'w+')
    for command in output:
        for line in command:
            print line
            f.write(line+'\n')
    f.close()


def TBD():


   #'''creates directory ig not exists'''

    os.mkdir(path, 0755)
    if not os.path.exists(ips):
        os.mkdir(ips, 0755)


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
