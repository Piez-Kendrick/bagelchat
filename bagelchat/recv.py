import os
import socket
import struct
import sys
import thread

'''
    # Recv
'''
class bagelchat_recv:
    chat_logs = []    
    NODE_ADDY = None
    socket_recv = None
    is_receiving = True
    
    def __init__(self, MULTICAST_ADDY, MULTICAST_PORT):
        self.NODE_ADDY = ('0.0.0.0', MULTICAST_PORT) # Listens to all interfaces

        # Create the socket
        self.socket_recv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Internet, UDP
        
        # Allows the port to be reused immediately instead of being stuck in the TIME_WAIT state
        self.socket_recv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Binds and listens to the node address
        self.socket_recv.bind(self.NODE_ADDY)

        # Tells the operating system to add the socket to the multicast group
        # on all interfaces
        GROUP = socket.inet_aton(MULTICAST_ADDY)
        MREQ = struct.pack('4sL', GROUP, socket.INADDR_ANY)
        self.socket_recv.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, MREQ)

    def recv_data(self):
        while True:            
            data, address = self.socket_recv.recvfrom(2048)
            self.chat_logs.append(('<%s>: %s' %(address[0], data)))
            
            # Clears the screen
            os.system('cls')
            
            # Prints everything in the log
            for chat_log in self.chat_logs:
                print chat_log