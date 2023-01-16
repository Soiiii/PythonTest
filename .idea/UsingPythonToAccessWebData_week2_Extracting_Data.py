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
x = 'From cwen@iupui.edu Fri Jan  4 16:10:39 2008 1'
y = refindall('\S+@\S+', x)
print(y)