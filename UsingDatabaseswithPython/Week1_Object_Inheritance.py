# When we make a new class - we can reuse an existing
# class and inherit all the capabilities of an existing class and
# then add our own little bit to make our new class
# Another form of store and reuse
# Write once - reuse many times
# Then new class (child) has all the capabilities of the old class (parent) - and then some more
from UsingDatabaseswithPython.Week1_Object_Life_Cycle import PartyAnimal2


class PartyAnimal2:
    x = 0
    name = ""
    def __init__(self, nam):
        self.name = nam
        print(self.name, "constructed")

    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)

class FootballFan(PartyAnimal2):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)

print('-------')
s = PartyAnimal2("Sally")
s.party()

j = FootballFan("Jim")
j.party()
j.touchdown()
# Sally constructed
# Sally party count 1
# Jim constructed
# Jim party count 1
# Jim party count 2
# Jim points 7

# class - cookie cutter, object - cookie
# Class - a template
# Attribute - A variable within a class
# Method - A function within a class
# Object - A particular instance of a class
# Constructor - Code that runs when an object is created
# Inheritance - The ability to extend a class to make a new class