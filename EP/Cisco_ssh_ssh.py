#!/usr/bin/python
import socket
import sys, os
import time
import datetime
from os import path

starttime = time.time()
ts=datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H_%M_%S')

#shows=['show clock']
shows=["show running","show ip int br","show ip route", "show ip protocols", "show clock","show platform", "show module", "show version", "show cdp ne", "show inventory | i PID"]
#login=["lions", "lions", "enable 15", "bonanza1947", "ter len 0"]
login=["ter len 0"]

# check how many arguments we got.  the first si the application the second should be username

if len(sys.argv) <=1:
    print "Usage: ssh.py <ip_address> <port>"
    sys.exit(0)
elif len(sys.argv) < 3:
    port=23
else:
    port=int(sys.argv[2])
ips=sys.argv[1]

path = ts
os.mkdir(path, 0755)
if not os.path.exists(ips):
    os.mkdir(ips, 0755)


#Create a Socket
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

print "\n Done running "+str(len(shows))+" Commands in " + str( time.time() - starttime)
print prompt