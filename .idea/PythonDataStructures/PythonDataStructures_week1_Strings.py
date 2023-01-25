# A String is a sequence of characters
# A string literal uses quotes 'Hello' or "Hello"
# For strings, + means "concatenate"
# When a string contains numbers, it is still a string
# We can convert numbers in a string into a number using int()
class Strings:
    str1 = "Hello"
    str2 = 'there'
    bob = str1 +str2
    print(bob)
    #Hellothere
    str3 = '123'
#    str3 = str3 + 1
# Traceback (most recent call last):
# File "", line 1, in <module>
# class Strings:
# File "", line 8, in Strings
# str3 = str3 + 1
# TypeError: can only concatenate str (not "int") to str
    x = int(str3) +1
    print(x)
    #124

#Reading and Converting
# name = input('Enter: ')
# print(name)
# apple = input('Enter: ') #100
# #x = apple - 10 #Error
# x = int(apple) - 10 #90
# print(x) #90


#Looking inside String
#We can get at any single character in a string using an index specified in square brackets
#The index value must be an integer and starts at zero
#The index value can be an expression that is computed

fruit = 'banana'
letter = fruit[1]
print(letter)
x=3
w=fruit[x-1]
print(w)
print(len(fruit))

#Looping Through Strings
# using a while statement and an iteration variable,
# and the len funciton, we can construct a loop to look at each of the letters
# in a string individually
index=0
while index< len(fruit):
    letter = fruit[index]
    print(index, letter)
    index += 1
    # Looping Through Strings
    # A definite loop using a for state is much more elegant
    # The iteration variable is completely taken care of by the for loop

for letter in fruit:
    print(letter)

#Looking Deeper into in
# The iteration varible "iterates" through the sequence (ordered set)
# The block(body) of code is executed once for each value in the sequence
# The iteration variables moves through all of the values in the sequence

for letters in 'banana':
    print('letters', letters)

    # Slicing Strings
    # We can also look at any continuous selection of a string using a colon operator
    # The second number is one beyond the end of the slice - "uup to but not including"
    # if the second number is beyond the end of the string, it stops at the end
s = 'Monty Python'
print(s[0:4]) #Mont
print(s[6:7]) #P
print(s[6:20]) #주어진 문자보다 큰 숫자 넣어도 됨
print(s[:2]) #Mo
print(s[8:]) #thon
print(s[:]) #Monty Python