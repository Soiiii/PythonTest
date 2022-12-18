#Arguments
#An argument is a value we pass into the function as its input when we call the function
#We use arguements so we can direct the function to do diffrent kinds of work when we call it at different times
#We put the arguments in parentheses after the name of the function
# big = max('Hello World' --> Argument )

class coursera6_1:
    x=5
    print('Hello')

    def print_lyrics():
        print("I'm a lumberjack, and I'm okay. ")
        print('I sleep all night and I work all day.')

    print('Yo')
    print_lyrics()
    x = x+2
    print(x)


#Parameters
#A parameter is a variable which we use in the function definition.
#It is a "handle" that allows the code in the function to access the arguments for a particular function invocation.

    def greet(lang):
        if lang == 'es':
            print('Hola')
        elif lang == 'fr':
            print('Bonjour')
        else:
            print('Hello')
    greet("en") #Hello
    greet('es') #Hola
    greet('fr') #Bonjour

#Return Values
#Often a function will take its arguments, do some computation,
# and return a value to be used as the value of the function call in the calling expression.
#The return keyword is used for this.

    def greet2():
        return "Hello"
    print(greet2(), 'Glenn') #Hello Glenn
    print(greet2(), "Sally") #Hello Sally

#Return Value
#A "fruitful" function is one that produces a result(or return value)
#The return statement ends the function execution and "sends back" the result of the function
