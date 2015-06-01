import os
import socket
import struct
import sys
import thread

from send import *
from recv import *

# Clears screen
os.system('cls')

# Multicast settings

MULTICAST_ADDY = '224.3.29.71'
MULTICAST_PORT = 32767

bc_send = bagelchat_send(MULTICAST_ADDY, MULTICAST_PORT)
bc_recv = bagelchat_recv(MULTICAST_ADDY, MULTICAST_PORT)
        

# Multithread

# Starts receiving data
try:
    thread.start_new_thread(bc_recv.recv_data, ())
    
except Exception as e:
    print e
   
# Waits for user input to send data
while True:
    bc_send.send_data(raw_input())
