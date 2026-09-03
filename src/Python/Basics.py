"""************************** Basics of Python ***************************"""

print("Hello World!")  # Print Hello World


#print a variable
message = "Hello Vairable World"
print(message)

#type , tells type 

a = 10
b = 19.95
print(type(a))
print(type(b))


#
print(5 / 2)

#It always gives us a float.

#The // operator gives us a result that's rounded down to the next integer.
print(5 // 2)



"""
Operator	Name	Description
a + b	Addition	Sum of a and b
a - b	Subtraction	Difference of a and b
a * b	Multiplication	Product of a and b
a / b	True division	Quotient of a and b
a // b	Floor division	Quotient of a and b, removing fractional parts
a % b	Modulus	Integer remainder after division of a by b
a ** b	Exponentiation	a raised to the power of b
-a	Negation	The negative of a
"""



#Order of operations
#The arithmetic we learned in primary school has conventions about the order 
# in which operations are evaluated. Some remember these by a mnemonic such as 
# PEMDAS - Parentheses, Exponents, Multiplication/Division, Addition/Subtraction.

print("add/sub",8 - 3 + 2) #ans is 7

print("add/sub",-3 + 4 * 2) #ans is 5

print("min",min(1, 2, 3))
print("max",max(1, 2, 3))

#abs returns the absolute value of an argument:
print("abs",abs(32))
print("-abs",abs(-32))

#In addition to being the names of Python's two main numerical types, int and float can also be called as functions which convert their arguments to the corresponding type:

print(float(10))
print(int(3.33))
# They can even be called on strings!
print(int('807') + 1)




"""Functions and Getting Help"""

#help(round)
#help(print)

"""Defining functions"""

def addition(a,b):
    #Python isn't smart enough to read my code and turn it into a nice English description. 
    # However, when I write a function, I can provide a description in what's called the docstring.
    """This functipon takes two numbers and adds them"""  #docstring
    return a + b

print("addition : ", addition(2,3))

#help(addition)



#Note: python has None instead of null ok

print(1, 2, 3, sep=' < ') #separater 

#But if we don't specify a value, sep is treated as having a default value of ' ' (a single space).
print(1, 2, 3)



#Functions that don't return¶
#Functions Applied to Functions¶




"""Booleans and Conditionals"""

x = True
print(x)
print(type(x))

"""
Comparison Operations
Operation	Description		Operation	Description
a == b	a equal to b		a != b	a not equal to b
a < b	a less than b		a > b	a greater than b
a <= b	a less than or equal to b		a >= b	a greater than or equal to b
"""

print(3.0 == 3) #True

print('3' == 3) #False, because one is a string and the other is an integer

#Remember to use == instead of = when making comparisons. 
#If you write n == 2 you are asking about the value of n. 
# When you write n = 2 you are changing the value of n.


#Q: Guess its value?
print("Guess ? ",True or True and False)

#Note: 'and' is evaluated before 'or'
#so for better visibility use parenthesis
print("Guess now ? ",True or (True and False))


#Conditionals
#Booleans are most useful when combined with conditional statements, 
# using the keywords if, elif, and else.

def positive_or_negative(x):
    if x == 0:
        print(x , " Is Zero")
    if x > 0:
        print(x," > 0") 
    if x < 0:
        print(x," < 0") 
    
positive_or_negative(0)
positive_or_negative(-1)
positive_or_negative(1)    
        

#Boolean conversion¶



"""Lists"""
primes = [2, 3, 5, 7]
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

#list of lists

hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K'], # (Comma after the last element is optional)
]
# (I could also have written this on one line, but it can get hard to read)
hands = [['J', 'Q', 'K'], ['2', '2', '2'], ['6', 'A', 'K']]


#A list can contain a mix of different types of variables:
my_favourite_things = [32, 'raindrops on roses', help]
# (Yes, Python's help function is *definitely* one of my favourite things)

print('planet at 0th index : ', planets[0])

#if you want the last element
print('planet at last index : ', planets[-1])

#if you want the 2nd last element
print('planet at 2nd last index : ', planets[-2])

#Slicing
#Imp rule --> list[start:end] , 
#here start is included, end is excluded


#find first 3 planets

print("first 3 planets : ", planets[0:3])

#find 2nd, 3rd and 4th planets

print("2nd, 3rd and 4th planets : ", planets[1:4])

#if our default is 0th indec only then another way to write 
print("first 3 planets 2: ", planets[:3])



#Q  "give me all the planets from index 3 onward"
print("give me all the planets from index 3 onward: ", planets[3:])

## All the planets except the first and last
print("All the planets except the first and last: ", planets[1:-1])

#Q # The last 3 planets
print("The last 3 planets: ", planets[-3:])



#Changing lists
#Lists are "mutable", meaning they can be modified "in place".

#One way to modify a list is to assign to an index or slice expression.


#let's say we want to rename Mars
planets[3] = 'Harsh'
print("planets : ", planets)

#shorten first 3 planet names
planets[:3]= ['Me', 'Ve', 'Ea']
print("planets v2 : ", planets)

#Some important list functions....

#length of list
print("length : ",len(planets))

## sort planets in alphabetical order , use sorted
print("sorted : ",sorted(planets)) #returns a new sorted list. It does not change the original names list.

#sum
print("sum primes : ", sum(primes))

#max and min
print("max primes : ", max(primes))
print("min primes : ", min(primes))





#### Interlude: objects

#In short, objects carry some things around with them. 
# You access that stuff using Python's dot syntax.

#A Python object has properties/data and methods, and you access them using a dot .

name = "Harsh"
print("upper : ",name.upper())  #method

#name        → object
#.upper()    → method belonging to that object

#List methods

#list.append modifies a list by adding an item to the end:

planets.append("Pluto")
print("append : ",planets)


#list.pop removes and returns the last element of a list:
planets.pop()  #removes last element
print("pop : ",planets)



###### Searching lists

#Where does Earth fall in the order of planets? 
#We can get its index using the list.index method.
print("planets : ",planets)
planets[3] = "Earth"
print("planets 276: ",planets)

earth_index = planets.index("Earth")
print("Earth index : ",earth_index)

#now lets find pluto

#pluto_index = planets.index("Pluto")  #gives ValueError as pluto is not in list
#print("pluto index : ",pluto_index)

## we got
"""File "/Users/harshveersinghnirwan/Downloads/Java-DSA-Practice/src/Python/Basics.py", line 283
    pluto-index = planets.index("Pluto")  #gives error as pluto is not in list
    ^^^^^^^^^^^
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?"""

#To avoid unpleasant surprises like this, 
#we can use the in operator to determine whether a list contains a particular value:

print("check pluto present ? : ", "Pluto" in planets)  #False