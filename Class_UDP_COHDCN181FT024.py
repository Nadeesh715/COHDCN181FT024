from ctype import *
import struct
import sys

class UDP(structure):
    _fields_=[("srcport",c_ushort),
              ("desport",c_ushort),
              ("len",c_long),
              ("checksum",c_long)
              ]


def __new__(self, socket_buffer = None):
    return self.from_buffer_copy(socket_buffer)



def __init__(self, socket_buffer= None):
    self.src_port=socket.inet_ntoa(struct.pack("@I",self.srcport))
    self.dest_port=socket.inet_ntoa(struct.pack("@I",self.destport))


print(ip.src_port)
