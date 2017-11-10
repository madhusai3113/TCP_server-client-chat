import socket
import sys
from threading import Thread

host = 'localhost'

port = 8888
#creating socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print "socket created"
#binding
try:
    s.bind((host, port))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()


print "socket bind complete"
#listening
s.listen(10)
print "socket listening"

while 1:
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    break

def reciving(connection):
    while 1:
        msg_recv = connection.recv(1024)
        print msg_recv

def sending(connection):
    while 1:
        msg = raw_input()
        connection.send(msg)

import time
#print reciving(conn)
t1 = Thread(target=reciving, args=(conn,))
t2 = Thread(target=sending, args=(conn,))
#sending(conn,msg)
t1.start()
t2.start()


s.close()