# ASCII
# American Standard Code for Information Interchange

# Representing Simple Strings
# Each character is represented by a number between 0 and 256 stored in 8 bits of memory
# We refer to "8 bits of memory as a "byte" of memory -
# (i.e my disk drive contains 3 Terabytes of memory)
# The ord() function tells us the numeric value of a simple ASCII character

print(ord('H')) #72
print(ord('e')) #101

#Unicode
#Multi-Byte Characters
#To represent the wide range of characters computers must handle we represent characters
# with more than one byte
# UTF-8(1-4 bytes) is recommended practice for encoding data to be exchanged between systems

#In Python3, all strings internally are Unicode
#Working with string variables in Python programs and reading data from files usually "just works"
#When we talk to a network resource using sockets or talk to a database we have to
# encode and decode data(usually to UTF-8)

#Python Strings to Bytes
# When we talk to an external resource like a network socket we sends bytes,
# so we need to encode Python 3 strings into a given character encoding
# When we read data from an external resource, we must decode it based on the
# character set so it is properly represented in Python 3 as a string

#Encode takes string and makes it into bytes
#Decode is a method in the bytes class ( bytes UTF-8 -> String Unicode)