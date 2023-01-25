# File Handle as a Sequence
# A file handle open for read can be treated as a sequence of strings
# where each line inthe file is a string in the sequence
# We can use the for statement to iterate through a sequence
# Remember - a sequence is an ordered set
xfile = open('/Users/baeksoyoung/Desktop/mbox.txt')
print(xfile.readline())
for cheese in xfile:
    print(cheese)

#Counting lines in a file
# Open a file read-only
# Use a for loop to read each line
# Count the lines and print out the number of lines
count=0
for line in xfile:
    count = count + 1
print('Line Count: ', count)

# Reading the whole file
# we can read the whole file(newlines and all) into a single string
fhand = open('/Users/baeksoyoung/Desktop/mbox.txt')
inp = fhand.read()
print(len(inp)) #11
print(inp[:20])

#Searching through a file
# We can put an if statement in our for loop to only print lines that meet some criteria
#We can strip the whitespace from the right-hand side of the string using rstrip() from the string lib
#The newline is considered "white space" and is stripped
fhand = open('/Users/baeksoyoung/Desktop/mbox.txt')
for line in fhand:
    line = line.rstrip() #delete nextline
    if line.startswith('abcd'):
        print(line, '??????') #abcd ?????

# Skipping with Continue
# We can conveniently skip a line by using the continue statement
fhand = open('/Users/baeksoyoung/Desktop/mbox.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('abcd'):
        continue
    print(line)

# Using in to select lines
# We can look for a string anywhere in a line as our selection criteria
print('Using')
fhand = open('/Users/baeksoyoung/Desktop/mbox.txt')
for line in fhand:
    line = line.rstrip()
    if not 'ab' in line:
        continue
print(line)

fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('abcd'):
        count = count+1
print('There were', count, 'Subject lines in ', fname)

#Bad File names
fname = input('Enter the file nam: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    quit()
count = 0
for line in fhand:
    if line.startswith('abcd'):
        count = count+1
print('There were', count, 'Subject lines in ', fname)
# Enter the file nam: d
# File cannot be opened:  d