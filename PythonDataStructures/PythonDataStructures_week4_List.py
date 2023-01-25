#What is not A "Collection??
#Most of our variables have one value in them -when we put a new value in the variable, the old valud is overwritten

#A list is a kind of collection
# A collection allows us to put many values in a single "variable"
# A collection is nice because we can carry many values around in one convenient package

# Squre Brackets is a list constant
#friends is a list of strings
friends = ['Joseph', 'Glenn', 'Sally']

#List Constants
# List constants are surrounded by quare brackets and the elements in the list are separated by commas
# A list element can be any Python object - even another list
# A list can be empty
print([1,24,75]) #[1, 24, 75]
print(['red', 'yellow', 'blue']) #['red', 'yellow', 'blue']
print([1,[3,2],4]) #[1, [3, 2], 4] -> 3 Elements in the list

#We already use lists!
for i in [6,5,4,3,2,1]:
    print(i)
print('Blast Off!')

#Lists and Definite Loops - Best pals
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends: #mnemonic variable
    print('Happy New Year', friend)
print('Done!')
#Happy New Year Joseph
# Happy New Year Glenn
# Happy New Year Sally
# Done!

# Looking inside Lists
# Just like strings, we can get at any single element in a list using an index specified in square brackets
friends = ['Joseph', 'Glenn', 'Sally']
print(friends[1]) #Glenn

#Lists are Mutable = Changeable
#Strings are not mutable
# Strings are 'immutable' - we cannot change the contents of a string - we must make a new string to make any change
#Lists are 'mutable' - we can change an element of a slit using the index operator
fruit = 'Banana'
# fruit[0] = 'b'
#Traceback (most recent call last):
# fruit[0] = 'b'
# TypeError: 'str' object does not support item assignment
x = fruit.lower()
print(x) #banana
lotto=[2,4,5,7,1]
print(lotto) #[2, 4, 5, 7, 1]
lotto[2]=3
print(lotto) #[2, 4, 3, 7, 1]

#How long is a list?
#THe len() function takes a list as a parameter and returns the number of elements in the list
#Actually len() tells us the number of elements of any set or sequence(such as a string)
greet = 'Hello'
print(len(greet)) #5
x = [1,2,'me',3]
print(len(x)) #4

#Using the Range function
# The range function returns a list of numbers that range from zero to one less than the parameter
# We can construct an index loop using for and an integer iterator
print(range(4))
print(len(friends))
print(range(len(friends)))