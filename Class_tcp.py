from ctype import *
import struct
import sys

class TCP(structure):
    _fields_=[("srcport",c_ushort),
              ("desport",c_ushort),
              ("seqnum",c_long),
              {"acknum",c_long),
              ("offset",c_ubyte,4),
              ("reserved",c_ubyte,4),
              ("flags",c_ushort),
              ("window",c_ubyte),
              ("checksum",c_ushort),
              ("urgpointer",c_short),
              ("tcpopt",c_long)
              ]


def __new__(self, socket_buffer = None):
    return self.from_buffer_copy(socket_buffer)



def __init__(self, socket_buffer= None):
    self.src_port=socket.inet_ntoa(struct.pack("@I",self.srcport))
    self.dest_port=socket.inet_ntoa(struct.pack("@I",self.destport))


print(ip.src_port)
