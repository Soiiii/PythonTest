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
