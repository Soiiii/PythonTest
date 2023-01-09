# Counting Pattern
counts = dict()
print('Enter a line of text: ') #Hello Hi How are you
line=input('')
words = line.split()
print('Words: ', words) #Words:  ['Hello', 'Hi', 'How', 'are', 'you']
print('Counting... ') #Counting...
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts', counts) #Counts {'Hello': 1, 'Hi': 1, 'How': 1, 'are': 1, 'you': 1}

# Definite Loops and Dictionaries
# Even though dictionaries are not stored in order, we can write a for loop
# that goes through all the entries in a dictionary - actually it goes
# through all of the keys in the dictionary and looks up the values
counts = {'chuck':1, 'fred':42,'jan':100}
for key in counts:
    print(key, counts[key])
# chuck 1
# fred 42
# jan 100

# Retrieving lists of keys and values
# You can get a list of keys, values, or items(both) from a dictionary
jjj = {'chuck':1, 'fred':42,'jan':100}
print(list(jjj)) #['chuck', 'fred', 'jan']
print(jjj.keys()) #dict_keys(['chuck', 'fred', 'jan'])
print(jjj.values()) #dict_values([1, 42, 100])
print(jjj.items()) #dict_items([('chuck', 1), ('fred', 42), ('jan', 100)])

#Two iteration Variables
# We loop through the key-value pairs in a dictionary using two iteration variables
# Each iteration, the first variable is the key and the second variable is the corresponding value for the key
jjj = {'chuck':1, 'fred':42,'jan':100}
for aaa,bbb in jjj.items():
    print(aaa, bbb)
# chuck 1
# fred 42
# jan 100

#/Users/baeksoyoung/Desktop/mbox.txt
name = input('Enter file: ')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)