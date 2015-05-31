from socket import *
import sys, time

UDP_IP='127.0.0.1'
UDP_PORT=5005

s=socket(AF_INET, # Internet
    SOCK_DGRAM) # UDP
    
s.bind((UDP_IP, 0))

s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

while 1:
    data=repr(time.time()) + '\n'
    s.sendto(data, (UDP_ID, UDP_PORT))
    time.sleep(2)