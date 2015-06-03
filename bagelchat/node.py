import os
import socket
import struct
import sys
import thread

from send import *
from recv import *

# Checks for usage help
if len(sys.argv) > 1:
    if sys.argv[1] == '-h' or sys.argv[1] == '--help':   
        print 'Usage: python setup.py [username] [multicast address] [multicast port]'
        print '#### All fields are optional ####'
        sys.exit()

# Clears screen
os.system('cls')

# Multicast settings
MULTICAST_USERNAME = str(sys.argv[1]) if len(sys.argv) > 1 else 'Anonymous'
MULTICAST_ADDY = str(sys.argv[2]) if len(sys.argv) > 2 else '224.3.29.71'
MULTICAST_PORT = int(sys.argv[3]) if len(sys.argv) > 3 else 32767

# Initializes bagelchat class
bc_send = bagelchat_send(MULTICAST_USERNAME, MULTICAST_ADDY, MULTICAST_PORT)
bc_recv = bagelchat_recv(MULTICAST_ADDY, MULTICAST_PORT)
        
# Multithreads to receive and send data
# Starts receiving data
try:
    thread.start_new_thread(bc_recv.recv_data, ())
    
except Exception as e:
    print e
   
# Keeps sending data
_data = None
while _data != '/quit':
    _data = raw_input()
    bc_send.send_data(_data)   