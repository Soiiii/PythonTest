# Opeaning a File
# Before we can read the contents of the file, we must tell Python
# which file we are going to work with and what we will be doing with the file
#
# This is done with the open() function
#
# open() returns a "file handle" - a variable used to perform opertaions on the filecmp
# Similar to "File -> Open" in a Word Processor

# Using open()
# handle = open(filename, mode)
# fhand = open('mbox.txt', 'r')
# returns a handle use to manipulate the filecmp
# filename is a string
# mode is optional and should be 'r' if we are planning to read the file and 'w' if we are going to write to the file

#The newline Character
# We use a special character called the "newline" to indicate when a line ends
# We represent it as \n in strings
# Newline is still one character - not two
stuff = 'Hello\nWorld!'
print(stuff)
# Hello
# World!
stuff = 'X\nY'
print(stuff)
#X
#Y
len(stuff)
print(len(stuff))
#3

# File Processing
# A text file can be thought of as a sequence of lines