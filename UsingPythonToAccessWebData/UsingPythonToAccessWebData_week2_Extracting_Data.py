# Matching and Extracting Data
# re.search() returns a True/False depending on whether the string matches the regular expresison
# If we actually want the matching strings to be extracted, we use re.findall()

import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
#[0-9]+ -> One or more digits
print(y) #['2', '19', '42']
y = re.findall('[AEIOU]+', x)
print(y) #[]

# Warning: Greedy Matching
# The repeat characters (* and +) push outward in both directions
# (greedy) to match the largest possible string

import re
x = 'From: using the : character'
y = re.findall('^F.+:', x)
#^F.+: -> ^F : First character in the match is an F
# . : any character
# + : One or more characters
# : : Last character in the match is a:
print(y) #['From: using the :']
#Greedy Matching says you're going to get back the larger thing

# Non-Greedy Matching
# Not all regular expression repeat codes are greedy! If you add a ? character,
# the + and * chill out a bit
# -> print out the shortest

import re
x = 'From: Using the : character'
y = re.findall('^F.+?:', x)
#^F.+?: -> ^F : First character in the match is an F
# . : any character
# + : One or more characters
# ?: : Last character in the match is a:
print(y) #['From:']

# Fine-Tuning String Extraction
# You can refind the match for re.findall() and separately determine which portion of the match is to be
# extracted by using parenthese
x = 'From stephen@iupui.edu Fri Jan  4 16:10:39 2008 1'
y = re.findall('\S+@\S+', x)
#\S : non-blank, whitespace character
print(y) #['stephen@iupui.edu']

#Parentheses are not part of the match - but they tell where to start and stop what string to extract
y = re.findall('\S+@\S+', x)
print(y)
y = re.findall('^From (\S+@\S+)', x)
print(y) #print(y) #

data = 'From stephen.marquard@uct.ac.za Fri Jan  4 16:10:39 2008 1'
atpos = data.find('@')
print(atpos, '?')
sppos = data.find(' ', atpos)
print(sppos)
host = data[atpos+1 : sppos]
print(host)

#The double split pattern
# Sometimes we split a line one way, and then grab one of the pieces of the line and split that piece again
line = 'From stephen@iupui.edu Fri Jan  4 16:10:39 2008 1'
words = line.split()
print(words) #['From', 'stephen@iupui.edu', 'Fri', 'Jan', '4', '16:10:39', '2008', '1']
email = words[1]
pieces = email.split('@')
print(pieces[1]) #iupui.edu

#The Regex Version
y = re.findall('@([^ ]*)', line)
#'@([^ ]*)'     "@" -> Look through the string until you find an at sign
# "[^ ] -> Match non-blank character
# * Match many of them

print(y) #['iupui.edu']

#Even Cooler Regex Version
import re
y = re.findall('^From . *@([^ ]*)', line)
#^From . *@([^ ]*)
#^          Starting at the beginning of the line
#From       Look for the string 'From '
#.          any number of characters
#*@         up to @
# (         begin extracting
# [^ ]      all the non blank characters
# )         extract
print(y)

#Escape Character
# If you want a special regular expression character to just behave
# normally (most of the time) you prefix it with '\'
import re
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+', x)
print(y) #['$10.00']
# \$[0-9.]+
# \$        A real dollar sign
# [0-9.]    One or more numbers and or dots, A digit or period
# +         At least one or more

lin = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
z = re.findall('\S+?@\S+', lin)
print(z) #['stephen.marquard@uct.ac.za']

x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)