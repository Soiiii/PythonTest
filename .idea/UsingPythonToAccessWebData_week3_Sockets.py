import socket

mysock = socket.socket((socket.AF_INET, socket.SOCK_STREAM))
mysock.connect(('data.pr4e.org', 80))
#There are strings inside of python that are in Unicode
#We have to send them out is what's called UTF-8
cmd = 'GET http://data.pr4e.org/remeo.txt HTTO/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if(len(data) < 1):
        break
    #Decode coverts it to the internal format called Unicode that runs inside
    print(data.decode())
mysock.close()