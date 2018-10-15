import socket
import sys, os
import time



def getdata(write)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Connect to the Server 'IP' and Port
    #s.connect(('10.56.100.1',23))
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
    prompt = s.recv(10)
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
        #f.write(command)
        fi = open(ips+'/'+"_".join(command.split())+"_"+path+".txt",'w+')
        fi.write("########" +command+"##########\n" )
        s.send (command + '\n')
        time.sleep(0.5)
        data = s.recv(65536)
        time.sleep(0.5)
        #print data
        # f.write(data)
        fi.write(data)
        #f.close()
        fi.close()
        print "Done.\n"
        time.sleep(0.5)
        s.recv(0)


