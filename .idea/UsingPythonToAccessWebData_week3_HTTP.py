#Hypertext Transfer Protocol(HTTP)
# Application Protocol
# Since TCP(and Python) gives us a reliable socket, what do we want to do with the socket?
# What problem do we want to solve?

# Application Protocols
# Mail, Wold Wide Web

#The dominant Application Layer Protocol on the Internet
#Invented for the Web - to Retrieve HTML, Images, Documents, etc
#Extended to be data in addition to documents - RSS, Web Services, etc..
#Basic Concept - Make a connection - Request a document - Retrieve the document - Close the Connection

# What is a Protocol?
# A set of rules that all parties follow so we can predict each other's behavior
# And not bump into each other
# On two-way roads in USA, drive on the right-hand side of the road
# On two-way roads in the UK, drive on the left-hand side of the road

# Getting Data From the Server
# Each the user clicks on an anchor tag with an href=value to switch to a new page,
# the browser makes a connection to the web server and issues a "GET" request -
# to Get the content of the page at the specified URL
# The server returns the HTML document to the Broswer which formats and displays the document to the user

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/remeo.txt HTTO/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if(len(data) < 1):
        break
    print(data.decode())
mysock.close()