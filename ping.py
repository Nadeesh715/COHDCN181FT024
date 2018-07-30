import socket
import struct
from ctypes import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("ip",nargs='?',type=str)
args = parser.parse_args()

class ipheader(Structure):

    _fields_ = [
        ("version", c_ubyte, 4),
        ("ihl", c_ubyte, 4),
        ("tos", c_ubyte),
        ("len", c_ushort),
        ("id", c_ushort),
        ("offset", c_ushort),
        ("ttl", c_ubyte),
        ("proto", c_ubyte),
        ("checksum", c_ushort),
        ("src", c_uint32),
        ("dst", c_uint32),
    ]

    def __new__(self, socket_buffer=None):
        return self.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer=None):

        self.TTL = str(self.ttl)

        self.src_address = socket.inet_ntoa(struct.pack("@I", self.src)) #convert network to host
        self.dst_address = socket.inet_ntoa(struct.pack("@I", self.dst))


def ipv4_pack():
    try:
        dst = args.ip
    except:
        print("Insert an IP address")
    src = '192.168.11.131'
    ip_vhl = 5
    ip_ver = 4
    ip_ver = (ip_ver << 4) + ip_vhl

    ip_dsc = 0
    ip_ecn = 0
    ip_tos = (ip_dsc << 2) + ip_ecn

    ip_tol = 0

    ip_idf = 54321

    ip_rsv = 0
    ip_dtf = 0
    ip_mrf = 0
    ip_frag_offset = 0

    ip_flg = (ip_rsv << 7) + (ip_dtf << 6) + (ip_mrf << 5) + ip_frag_offset

    ip_ttl = 255

    ip_proto = socket.IPPROTO_ICMP

    ip_chk = 0

    ip_saddr = socket.inet_aton(src)
    
    ip_daddr = socket.inet_aton(dst)

    ippack = struct.pack("!BBHHHBBH4s4s",ip_ver, ip_tos, ip_tol, ip_idf, ip_flg, ip_ttl, ip_proto, ip_chk, ip_saddr, ip_daddr)

    return src, dst, ippack

try:
    s= socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(3))
    
except:
    print("socket cant be created")

try:
    (src, dst, ippack) = ipv4_pack()
except:
    print("Invalid usage")
    exit(0)
while True:
    s.sendto(ippack, (dst, 0))
    data = sock.recv(1024)
    ip = ipheader(data[14:])
    print("Reply From " + ip.dst_address + ": " + "TTL=" + ip.TTL)
