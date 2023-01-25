# What is a collection?
# A collection is nice because we can put more than one value in it and carry them all around in one convenient package
# We have a bunch of values in a single 'Variable'
# We do this by having more than one place 'in' the variable
# We have ways of finding the different places in the variable

# What is not a collection?
# Most of our variables have one value in them - when we put a new value in the variable
# - the old value is overwritten

#list - A linear collection of vlaues that stay in order
#Dictionary - A 'bag' of values, each with its own label

# Dictionaries
# Python's most powerful data collection
# Dictionaries allow us to do fast database-like operations in Python
# Dictionaries have different names in different languages
# -Associative Arrays : Perl/PHP
# -Properties or map or hashmap: Java

# Lists index their entreis based on the position in the list
# Dictionaries are like bags - no order
# So we index the things we put in the dictionary with a "lookup tag"

purse = dict()
purse['money']=12
purse['candy']=3
purse['tissues'] = 75
print(purse) #{'money': 12, 'candy': 3, 'tissues': 75}
print(purse['candy']) #3
purse['candy'] = purse['candy'] + 2
print(purse) #{'money': 12, 'candy': 5, 'tissues': 75}

# Comparing lists and dictionaries
# Dictionaries are like lists except that they use keys instead of numbers to look up values

lst = list()
lst.append(21)
lst.append(183)
print(lst) #[21, 183]
print(lst[0]) #21

ddd = dict()
ddd['age'] = 21
ddd['course'] = 182
print(ddd) #{'age': 21, 'course': 182}
print(ddd['age']) #21

# Dictionary Literals (Constants)
# Dictionary literals use curly braces and have a list of key :value pairs
# You can make an empty dictionary using empty curly braces
jjj = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
print(jjj)