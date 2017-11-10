import socket
import time
from threading import Thread

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 8888))

def reciving(connection):
    while 1:
        msg_recv = connection.recv(1024)
        print msg_recv

def sending(connection):
    while 1:
        msg = raw_input()
        connection.send(msg)



#print reciving(conn)
#msg = raw_input('')
t1 = Thread(target=reciving, args=(clientsocket,))

t2 = Thread(target=sending, args=(clientsocket,))
#sending(conn,msg)
t1.start()
t2.start()