import os
import socket
import struct
import sys
import thread
from cipher import *

'''
    # Recv
'''
class bagelchat_recv:  
    users_online = 0
    username_list = []
    username_dict = {}
    
    # Constructor
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

    # Destructor
    def __del__(self):
        # Closes and shutdowns socket
        self.socket_recv.shutdown(socket.SHUT_WR)
        self.socket_recv.close()
        
    # returns recv data (for GUI)        
    def get_recv_data(self):                        
        data, address = self.socket_recv.recvfrom(2048)
        # If data is not handshake key, we treat it as a normal key
        if HANDSHAKE_KEY_JOIN not in mutlicast_decrypt(data) and HANDSHAKE_KEY_QUIT not in mutlicast_decrypt(data):
            return ('<%s> %s' %(address[0], mutlicast_decrypt(data))), False, self.users_online
        
        # else its a new user, and we need to update the number of users online
        # check for the received username in our existing database
        # if its not in our existing database then its a new user
        # and we need to send our own handshake
        else:
            _user_enter_exit = False            
            _username = mutlicast_decrypt(data)[0:mutlicast_decrypt(data).find(':')]                        
            
            # If we received a handshake key to 'join'
            if HANDSHAKE_KEY_JOIN in mutlicast_decrypt(data):  
                # If its a new user
                if _username not in self.username_list:
                    self.username_list.append(_username)
                    self.users_online = len(self.username_list)                       
                    _user_enter_exit = True
                
                # Refresh existing user's responding dictionary
                self.username_dict[_username] = 0
                    
            # If a user leaves chat group
            elif HANDSHAKE_KEY_QUIT in mutlicast_decrypt(data):
                if _username in self.username_list:
                    self.username_list.remove(_username)
                    self.users_online = len(self.username_list)
                    self.username_dict.__delitem__(_username)
                    _user_enter_exit = True  
                    
            # Refresh data base to check if any user hasn't been responding for > 5 handshakes
            for username in self.username_list:                
                self.username_dict[username] += 1
                
            return None, _user_enter_exit, self.users_online