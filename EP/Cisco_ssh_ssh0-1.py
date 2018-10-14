#!/usr/bin/python
import socket
import sys
import time

shows=["show running","show ip int br", "show clock", "show module", "show version"]
login=["lions", "lions", "enable 15", "bonanza1947", "ter len 0"]

# check how many arguments we got.  the first si the application the second should be username
if len(sys.argv) <=1:
	print "Usage: ssh.py <ip_address> <port>"
	sys.exit(0)
elif len(sys.argv) < 3:
	port=23
else:
	port=int(sys.argv[2])
ips=sys.argv[1]


#Create a Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Connect to the Server 'IP' and Port
#s.connect(('10.56.100.1',23))
print "Connecting to "+ips+":"+ str(port)
s.connect((ips,port))
#time.sleep (2)
#Receive the banner
#data = s.recv(1024)
#print data
#time.sleep(1)

#  Username
#s.send('lions'+'\r\n')
#time.sleep(0.5)
#data = s.recv(1024)
#print data

# Password
#s.send('lions'+'\r\n')
#time.sleep(0.5)
#data = s.recv(1024)
#print data

#s.send('enable 15' + '\r\n')
#time.sleep(0.5)
#data = s.recv(1024)

#s.send('bonanza1947' + '\r\n')
#time.sleep(0.5)
#data = s.recv(1024)

#s.send('ter len 0' + '\r\n')
#time.sleep(0.5)
#data = s.recv(1024)


for command in login:
    s.send (command + '\r\n')
    time.sleep(0.3)


print "####Login complete###"

#s.send('show ip int br'+'\r\n')
#time.sleep(0.5)
#data = s.recv(8192)
#print data

for command in shows:
  s.send (command + '\r\n')
  time.sleep(1.5)
  data = s.recv(32768)
  time.sleep(0.5)
  print data
  time.sleep(1)