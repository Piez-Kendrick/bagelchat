import socket
import struct
import sys
import thread

'''
    # Send
'''
class bagelchat_send:
    MULTICAST_GROUP = None
    socket_send = None

    def __init__(self, MULTICAST_ADDY, MULTICAST_PORT):
        self.MULTICAST_GROUP = (MULTICAST_ADDY, MULTICAST_PORT)

        # Create the datagram socket
        self.socket_send = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Set a timeout so the socket does not block indefinitely when trying to
        # receive data
        self.socket_send.settimeout(0.2)

        # Set the time-to-live for messages to 1 so they do not go past the
        # local network segment
        TTL = struct.pack('b', 1)
        self.socket_send.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, TTL)

    def send_data(self, _data):
        sent = self.socket_send.sendto(_data, self.MULTICAST_GROUP)