#!/usr/bin/python
import socket
import sys, os
import time
import datetime
from os import path


ts=datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H_%M_%S')

shows=['show clock']
#shows=["show running","show ip int br", "show clock", "show module", "show version", "show cdp ne", "show inventory | i PID"]
login=["lions", "lions", "enable 15", "bonanza1947", "ter len 0"]


# check how many arguments we got.  the first si the application the second should be username


path = ts
os.mkdir(path, 0755)
if not os.path.exists(ips):
    os.mkdir(ips, 0755)

ips = 10.56.100.1
port = 23
#Create a Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Connect to the Server 'IP' and Port
#s.connect(('10.56.100.1',23))
print "Connecting to "+ips+":"+ str(port)
s.connect((ips,port))


for command in login:
    s.send (command + '\r\n')
    time.sleep(0.3)

f = open(path+'/'+ips+"_"+"login"+".txt",'wr')
data = s.recv(1024)
f.write(data)
print "####Login complete###\n"

data = s.recv(0)
#s.send('show ip int br'+'\r\n')
s.send ('\r\n')
s.send ('\r\n')
prompt = s.recv(32)
print prompt
s.send ('\r')
time.sleep(0.5)
#data = s.recv(8192)
#print data
data = s.recv (0)
print ts


s.recv(0)

print "DATA =" + data  + '\n'

for command in shows:
    print 'running '+command+".."
    f = open(path+'/'+ips+"_"+"_".join(command.split())+".txt",'wr')
    f.write(command)
    fi = open(ips+'/'+"_".join(command.split())+"_"+path+".txt",'wr')
    fi.write(command)
    s.send (command + '\r\n')
    time.sleep(1.5)
    data = s.recv(65536)
    time.sleep(0.5)
    #print data
    f.write(data)
    fi.write(data)
    f.close()
    fi.close()
    print ".done\n"
    time.sleep(1)
    s.recv(0)


print ts

print prompt