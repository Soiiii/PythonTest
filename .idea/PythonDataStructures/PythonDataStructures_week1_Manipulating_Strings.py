# String Concatenation
# When the + operator is applied to strings, it means "concatenation"

a = 'Hello'
b = a + 'There'
print(b) #HelloThere
c = a + ' ' + 'There'
print(c) #Hello There

#Using in as a Logical Operator
#The in keyword can also be used to check to see if one string is "in" another string
#The in expression is a logical expression that returns True or False and can be used in an if statement
fruit = 'banana'
'n' in fruit
if 'a' in fruit:
    print('Found it!') #Found it

#String Library
#Python has a number of string functions which are in the string library
#These functions are already built into every string - we invoke them by appending the function to the string variable
#These functions do not modify the original string, instead they return a new string that has been altered
greet = 'Hello Bob'
zap = greet.lower()
print(zap) #hello bo
print(greet) #Hello Bob

#Searching a String
# We use the find() function to search for a substring whithin another string
# find() finds the first occurence of the substring
# If the substring is not found, find() returns -1
# Remember that string position starts at zero
fruits = 'banana'
pos = fruit.find('na') #2
print(pos)
aa = fruit.find('z')
print(aa) #-1


#Search and Replace
# The replace() function is like a "search and replace" operation in a word processor
# It replaces all occurrences of the search string with the replacement string
greet = 'Hello Bob'
nstr = greet.replace('Bob', 'Jane')
print(nstr) #Hello Jane
nstr = greet.replace('o', 'X')
print(nstr) #HellX BXb

#Stripping Whitespace
# Sometimes we want to take a string and remove whitespace at the beginning and/or calendar
# lstrip() and rstrip() remove whitespace at the left and right
# strip() removes both beginning and ending whitespace
greet = '   Hello Bob      '
greet.lstrip() #'Hello Bob      '
greet.rstrip()#'   Hello Bob'
greet.strip() #'Hello Bob'

#Parsing and Extracting
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 -0:14:16 2022'
atpos = data.find('@')
print(atpos) #21
sppos = data.find(' ', atpos) #여기서의 atpos는 시작위치를 설정하는것
print(sppos) #31
host = data[atpos+1 : sppos]
print(host) #uct.ac.za

