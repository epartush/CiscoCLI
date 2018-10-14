#!/usr/bin/python
import time

a = 12

for i in range (1, a, 1):
    print (a - i)* ' ' + i * '*' + (i-1) * '*'



for i in range (1,a,1):
    print '# '

print time.time()