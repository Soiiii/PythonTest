# The Regular Expression Module
# Before you can use regular expresisons in your program, you must import the library using "import re"
# You can use re.search() to see if a string matches a regular expression,
# similar to using the find() method for strings
# You can use re.findall() to extract portions of a string that match your regular expression, similar to a
# combination of find() and slicing:var[5:10]

# Using re.search() like find()
hand = open('/Users/baeksoyoung/Desktop/mbox.txt')
for line in hand:
    line = line.rstrip()
    if line.find('From ') >= 0:
        print(line)

import re

hand = open('/Users/baeksoyoung/Desktop/mbox.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From ', line):
        print(line)

# Using re.search() like startswith()
hand = open('/Users/baeksoyoung/Desktop/mbox.txt')
for line in hand:
    line.rstrip()
    if line.startswith('From '):
        print('Startswith',line)

import re
hand = open('/Users/baeksoyoung/Desktop/mbox.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From ', line):
        # ^ -> Carrot Character
        #^from -> f is the first of the line
        print(line)

# Wild-Card Characters
# The dot character matches any character
# If you add the asterisk character, the character is "any number of times"
# ^X.* -> . : any character, * : 0 or more time

# Fine-Tuning Your Match
# Depending on how "clean" your data is and the purpose of your application,
# you may want to narrow your match down a bit
# ^X.*:
# ^ : Match the start of the line
# . : Match any character
# * : Many times

# ^X-\S+:
# ^ : Match the start of the line
# \S : Match any non-whitespace character
# + : One or more times
# ex) X-Sieve: (True), X-Plane is behind ~~ : (False -> There is whitespace before colon)