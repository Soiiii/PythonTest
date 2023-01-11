# Tuples are like lists
# tuples are another kind of sequence that functions much like a list
# they have elements which are indexted starting at 0

x=('Glenn', 'Sally', 'Joseph')
print(x[2]) #Joseph
y = (1, 9, 2)
print(y) #(1, 9, 2)
print(max(y)) #9

# but Tuples are "immutable"
# Unlike a list, once you create a tuple, you cannot alter its contents - similar to string

x = [9, 8, 7]
x[2] = 6
print(x) #[9, 8, 6]

# y = 'ABC'
# y[2] = 'D' #error
# z = (5,4,3)
# z[2] = 0 #error

# Tuples are more efficient
# Since Python does not have to build tuple structures to be modifiable, they are simpler and more efficient in terms
# memory use and performance than lists
# So in our program when we are making 'temporary variables' we prefer tuples over lists

# Tuples and Assignmnet
# We can also put a tuple on the left-hand side of an assignment statement
# We can even omit the parentheses
(x,y) = (4, 'fred')
print(y) #fred
(a,b) = (99, 98)
print(a) #99

# Tuples and Dictionaries
# The item() method in dictionaries returns a list of (key, value) tuples
d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k,v) in d.items():
    print(k,v)
# csev 2
# cwen 4
tups = d.items()
print(tups) #dict_items([('csev', 2), ('cwen', 4)])

# Tuples are Comparable
# The comparison operators work with tuples and other sequences.
# If the first item is equal, Python goes on to the next element,
# and so on, until it finds elements that differ
print((0,1,2)<(5,1,2)) #True
print(('Sally', 'Joseph')<('Sally', 'Adams')) #False

# Sorting Lists of tuples
# We can take adavantage of the ability to sort a list of uples to get a sorted version of a dictionary
# First we sort the dictionary by the key using the items() method and sorted() function
#In dictionaries, you can't have two keys. You can put the same values
d = {'b':1, 'a':10, 'c':22}
print(sorted(d.items())) #[('a', 10), ('b', 1), ('c', 22)]

# Using sorted()
# We can do this even more directly using the built-in function sorted that takes a sequence as a parameter
# and returns a sorted sequence
d = {'b':1, 'a':1, 'c':22}
t = sorted(d.items())
print(t) #[('a', 1), ('b', 1), ('c', 22)]
for k,v in sorted(d.items()):
    print(k,v)
# a 1
# b 1
# c 22

# Sort by values instead of keys
# If we could construct a list of tuples of the form(value, key) we could sort by value
# We do this with a for loop that creates a list of tuples
c = {'b':1, 'a':10, 'c':22}
tmp = list()
for k,v in c.items():
    tmp.append((v,k))
print(tmp) #[(1, 'b'), (10, 'a'), (22, 'c')]
tmp = sorted(tmp, reverse=True)
print(tmp) #[(22, 'c'), (10, 'a'), (1, 'b')]

#The top 10 most common words
fhand = open('/Users/baeksoyoung/Desktop/mbox.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
for val, key in lst[:10]:
    print(key, val)

#Shorter version
# List comprehension creates a dynamic list.
# In this case, we make a list of reversed tuples and then sort it
c = {'a':10, 'b':1, 'c':22}
print(sorted([(v,k) for k,v in c.items()])) #[(1, 'b'), (10, 'a'), (22, 'c')]
# lst = list()
# for key, val in counts.items():
#     newtup = (val, key)
#     lst.append(newtup)
# ===== (v,k) for k,v in c.items() 위에 4줄과 이 한줄이 같은 의미

#<Summary>
#Tuple syntax
# Immutability
# Comparability
# Sorting
# Tuples in assignment statements
# Sorting dictionaries by either key or value