# Concatenating Lists Using
# We can create a new list by adding two existing lists together
a = [1,2,3]
b= [4,5,6]
c = a + b
print(c) #[1, 2, 3, 4, 5, 6]
print(a) #[1, 2, 3]
#Lists can be sliced using:
#Remember: Just like in strings, the second number is "up to but not including"
print(c[3:]) #[4, 5, 6]
print(c[:]) #[1, 2, 3, 4, 5, 6]
print(c[:4]) #[1, 2, 3]

#Building a List from Scratch
#We can create an empty list and then add elements using the append method
# The list stays in order and enw elements are added at the end of the list
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff) #['book', 99]
stuff.append('cookie')
print(stuff) #['book', 99, 'cookie']

#Is someting in a list?
# Python provides two operators that let you check if an item is in a list
# These are logical operators that return True or False
# They do not modify the list
# append -> add to the end
some = [1,9,21,10.16]
print(9 in some) #True
print(15 in some) #False
print(20 not in some) #True

# Lists are in Order
# A list can hold many items and keeps those items in the order until we do something to change the order
# A list can be sorted (i.e., change its order)
# The sort method(unlike in strings) means "sort yourself"
friends = ['Joe', 'Mike', 'Tim', 'Abe']
friends.sort()
print(friends) #['Abe', 'Joe', 'Mike', 'Tim']
print(friends[1]) #Joe

# #Built-in Functions and Lists
# There are a number of functions built in Python that take lists as parameters
# Remember the loops we built? These are much simpler
nums = [3, 41, 21, 9, 2, 1]
print(len(nums)) #6
print(max(nums)) #41
print(min(nums)) #1
print(sum(nums)) #77

#Best Friends: Lists and Strings
#Split breaks a string into parts and produces a list of strings.
# We think of these as words. We can access a particular word or loop through all the words
abc = 'With three words' #Strings
stuff = abc.split()
print(stuff) #['With', 'three', 'words']

#Split - when you do not specify a delimiter, multiple spaces are trated like one delimiter
#You can specify what delimiter character to use in the splitting
line = 'A lot                  of spaces'
etc = line.split()
print(etc) #['A', 'lot', 'of', 'spaces']
line = 'first;second;third'
thing = line.split(';')
print(thing) #['first', 'second', 'third']

#The double split Pattern
#Sometimes we split a line one way, and then grab one of the pieces of the line and split that piece again
line = 'From stephen.marquard@uct.ac.za Sat Jan   5'
words = line.split()
email = words[1]
pieces = email.split('@')
print(pieces[1]) #uct.ac.za

# List Summary
# Concept of a collection
# Lists and definite loops
# Indexing and lookup
# List mutability
# Functions : len, min, max, sum
# Slicing lists
# List methods : append, remove
# Sorting lists
# Splitting strings into lists of words
# Using split to parse strings

fruit = 'Banana'
fruit[0] = 'b'
print(fruit)