# Object Liftcycle
# Objects are created, used and discarded
# We have special blocks of code (methods) that get called
# At the moment of creation(constructor)
# At the moment of destruction(destructor)
# Constructors are used a lot
# Deconstructors are seldom used

# Constructor
# The primary purpose of the constructor is to set up some
# instnace variables to have the proper initial values when
# the object is created

class PartyAnimal:
    x = 0

    def __init__(self):
        print("I am constructed")

    def party(self):
        self.x = self.x +1
        print('So far', self.x)

    def __del__(self):
        print("I am destructed", self.x)

an = PartyAnimal()
#I am constructed
an.party() #So far 1
an.party() #So far 2
#I am destructed 2
an = 42
print('an contains', an) #an contains 42

# The constructor and destructor are optional. The constructor is typically
# sued to set up variables. The desructor is seldom used

#Constructors
#In object oriented programming, a constructor in a class is a special
# block of statements called when an object is created

#Many Instance
# We can create lots of objects - the class is the template for the object
# We can store each distinct object in itws own variable
# We call this having multiple instances of the same class
# Each instance has its own copy of the instance variables

class PartyAnimal2:
    x = 0
    name = ""
    def __init__(self,z):
        self.name = z
        print(self.name, "constructed")
    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)
# Sally constructed
s = PartyAnimal2("Sally")
# Sally party count 1
s.party()

# jim constructed
j = PartyAnimal2("jim")
# jim party count 1
j.party()
# Sally party count 2
s.party()

#We have two independent instances