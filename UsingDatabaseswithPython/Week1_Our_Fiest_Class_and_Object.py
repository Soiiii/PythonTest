# class is a reserved word
class PartyAnimal:
    x=0

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)
#Construct a PartyAnimal object and store in an variable
an = PartyAnimal()

# PartyAnimal.party(an)
an.party() #So far 1
an.party() #So far 2
an.party() #So far 3

#Playing with dir() and type()
# The dir() command lists capabilities
# Ignore the ones with underscores - these are used by Python itself
# The rest are real operations that the object can perform
# It is like type() - it tells us something "about" a variable

print("Type", type(an))
# Type <class '__main__.PartyAnimal'>
print("Dir", dir(an))
# Dir ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__',
# '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
# '__subclasshook__', '__weakref__', 'party', 'x']