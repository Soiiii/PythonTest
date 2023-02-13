# ASCII American Standard Code for Information Interchange
# Representing Simple Strings
# Each character is represented by a number between 0 and 256 stored in 8
# bits of memory
# We refer to "8 bits of memory as a "byte" of memory - (i.e. my disk drive "
# contains 3 Terabytes of memory)
# The ord() function tells us the numeric value of a simple ASCII char and it's called
# ord which stands for ordinal. What's the ordinal?

# Multi-Byte Characters
# To represent the wide range of characters computers must handle we represnet
# characters with more than one byte
# UTF-16 FIXED LENGTH 2 bytes
# UTF-32 FIXED LENGTH 4 bytes
# UTF-8 1-4 bytes
# Upwards compatible with ASCII
# Automatic detection between ASCII and UTF-8
# UTF-8 is recommended practice for encoding data to be exchanged between systems

x = b'abc'
print(type(x)) #<class 'bytes'>
x = '광춘'
print(type(x)) #<class 'str'>
x = u'이광춘'
print(type(x)) #<class 'str'>

# Python3 and Unicode
# In Python 3, all strings internally are UNICODE
# Working with string variables in Python programs and reading
# data from files usually "just works"
# When we talk to a network resouce using sockets or talk to a database
# we have to encode and decode data(usually to UTF-8)

# Python Strings to Bytes
# When we talk to an external resource like a network socket we sends bytes,
# so we need to encode Python 3 strings into a given character encoding
# When we read data from an external source, we must decode it based on the character set
# so it is properly represented in Python3 as a string

# An HTTP Request in Python
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
# Encode: takes this string and makes it into bytes
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if(len(data)<1):
        break
    print(data.decode())
mysock.close()