import socket
import sys
import argparse
from threading import *

parser = argparse.ArgumentParser()
parser.add_argument("-l","--ip",type=str)
parser.add_argument("-p","--port",type=int)
args = parser.parse_args()

def server():
    print("This is he Server!")
    print("Server connected to : " +args.ip + " : " + str(args.port))
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.bind((args.ip, args.port))
    mysocket.listen(1)
    
    t2=Thread(target=client)
    t2.start()
    
    conn, addr = mysocket.accept()
   
    print("Connected to: " + addr[0]+ " : " + str(addr[1])+"\n....")
    conn.send("This message from server".encode("utf-8"))
    data = conn.recv(2048)
    print (data.decode("utf-8"))
    mysocket.close()


def client():
    print("This is the client!")
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.connect((args.ip , args.port))
    data = mysocket.recv(2048)
    print (data.decode("utf-8"))
    mysocket.send("this message is from client".encode("utf-8"))
    mysocket.close()

server()
#client()

#t1=Thread(target=server)
#t1.start()
#t2=Thread(target=client)
#t2.start()

