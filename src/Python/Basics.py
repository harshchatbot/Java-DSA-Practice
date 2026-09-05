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


#def is a Python keyword meaning define a function.
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

######Tuples

#Tuples
#Tuples are almost exactly the same as lists. They differ in just two ways.

#1: The syntax for creating them uses parentheses instead of square brackets
#2: They cannot be modified (they are immutable).

t = (1, 2, 3)
print("tuple : ", t)

t2 = 1, 2, 3 # equivalent to above
print("tuple2 : ", t2)

#try to modify

# t[0] = 100 #TypeError: 'tuple' object does not support item assignment

#but we can access the elemets like list:
print(t[0])  # 1

#What is the usage of Tuples?
#Use a tuple when you want to group a fixed set of related values that should not change.

#simpley when you dont want to change the data, you want to work on some fixed record/data


x = 0.125
print("tuple 1 : ", x.as_integer_ratio()) #returns multiple values i.e here numerator and denominator

#or

numerator , denominator = x.as_integer_ratio()
print("tuple2 numerator: ", numerator , "denominator : ", denominator)

#suppose we want to swap two variables, but we dont want to use a third variable,so, we can do it in one line using a tuple:
a = 10
b = 20
a,b = b,a
print("tuple swap a= ", a,"b = ", b)




"""Loops and List Comprehensions"""

#Loops are a way to repeatedly execute some code.

for planet in planets:
    print(planet, end=' ') # prints on same line as end=''

print()   # move to next line

#The for loop specifies

#the variable name to use (in this case, planet)
#the set of values to loop over (in this case, planets)

#You can even loop through each character in a string:


text = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'

# print all the uppercase letters in s, one at a time
for char in text:
    if char.isupper():
        print(char, end=' ')

print()   # move to next line


#range()
#range() is a function that returns a sequence of numbers. It turns out to be very useful for writing loops.

#For example, if we want to repeat some action 5 times:

for i in range(5):
    print("lets loop this 5 times : ", i)



#while loops
#The other type of loop in Python is a while loop, which iterates until some condition is met:

i = 0
while i < 5:
    print("while looping : ",i)
    i += 1  # i = i + 1


######## List comprehensions

#List comprehension = a short way to create a new list using a loop.

#one way of doing this
squares = []
for sq in range(5):
    squares.append(sq**2)
print("squares : ", squares)  


#now making this shorted using list comprehensions

squares2 = [sq**2 for sq in range(5)]
print("squares2 : ", squares2)  

#We can also add an if condition:

squares3 = [sq**2 for sq in range(5) if sq <= 3]
print("squares3 : ", squares3)  
#better formatting for visibility

print([
    sq**2
    for sq in range(5)
    if sq <= 2
])



###########  Zen of Python  #########

#The Zen of Python is a collection of 19 "guiding principles" for writing computer programs that influence the design of the Python programming language.
#[1] Python code that aligns with these principles is often referred to as "Pythonic".[2]

nums = [5,8,9,3,7,2,1]
def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    for num in nums:
        print("num : ", nums.index(num))
        if num % 7 == 0:
            return True
        

    # after loop finishes
    return False

print("has_lucky_number : ", has_lucky_number(nums))



"""
R and Python have some libraries (like numpy and pandas) 
compare each element of the list to 2 (i.e. do an 'element-wise' comparison) 
and give us a list of booleans like [False, False, True, True].

Implement a function that reproduces this behaviour, 
returning a list of booleans corresponding to whether the corresponding element 
is greater than n.
"""

def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.
    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    result = []
    for i in L:
        if i > thresh:
            result.append(True)
        else:
            result.append(False)    

    #return complete list once the loop finishes
    return result
        
print("elementwise_greater_than : ", elementwise_greater_than([1, 2, 3, 4], 2))        


#And here's the list comprehension version:

def elementwise_greater_than2(L2, thresh2):
    return [i > thresh2 for i in L2]


print("elementwise_greater_than2 : ", elementwise_greater_than2([1, 2, 3, 4], 2))   






##

meals = ["Pizza", "Burger", "Burger", "Pasta"]

def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    for i in range(len(meals) - 1):
        if meals[i] == meals[i+1]:
            return True
    return False

print("meals : ", menu_is_boring(meals))





####Monte Carlo method
#Next to the Blackjack table, the Python Challenge Casino has a slot machine. 
#You can get a result from the slot machine by calling play_slot_machine(). 
# The number it returns is your winnings in dollars. Usually it returns 0. 
# But sometimes you'll get lucky and get a big payday. Try running it below:
#each play costs $1


import random

def play_slot_machine():
    outcomes = [0, 0, 0, 0, 2, 5, 10]
    return random.choice(outcomes)



def estimate_average_slot_payout(n_runs):
    """Run the slot machine n_runs times and return the average net profit per run.
    Example calls (note that return value is nondeterministic!):
    >>> estimate_average_slot_payout(1)
    -1
    >>> estimate_average_slot_payout(1)
    0.5
    """
    #think of this in 4 steps
    total_profit = 0 #store total profit

    #run machine n_runs times
    for i in range(n_runs):
        payout = play_slot_machine()
        net_profit = payout - 1
        total_profit += net_profit  # this += is just shorthand of total_profit = total_profit + net_profit
        
    Avg_profit = total_profit / n_runs

    return Avg_profit    


print("estimate avg profit : ", estimate_average_slot_payout(5))


#here we did mistake in naming convention :
#Avg_profit should be avg_profit as in python
#Python variable naming convention is generally snake_case with lowercase letters.











"""Strings and Dictionaries"""


#Strings
##One place where the Python language really shines is in the manipulation of strings. This section will cover some of Python's built-in string methods and formatting operations.

#Such string manipulation patterns come up often in the context of data science work.

x = 'Pluto is a planet'
y = "Pluto is a planet"
print("strings : ",x == y)

print("Pluto's a planet!")
print('My dog is named "Pluto"')

print('Pluto\'s a planet!')  #escape character

"""
The table below summarizes some important uses of the backslash character.

What you type...	What you get	example	print(example)
\'	'	'What\'s up?'	What's up?
\"	"	"That's \"cool\""	That's "cool"
\\	\	"Look, a mountain: /\\"	Look, a mountain: /\
\n	
"1\n2 3"	1
2 3
"""

hello = "hello\nworld"
print(hello)

triplequoted_hello = """hello
world"""
print(triplequoted_hello)
triplequoted_hello == hello



#The print() function automatically adds a newline character unless we specify a value for the keyword argument end other than the default value of '\n':

print("hello4")
print("world4")
print("hello4", end='')
print("pluto4", end='')



#Strings are sequences
#Strings can be thought of as sequences of characters. Almost everything we've seen that we can do to a list, we can also do to a string.

# Indexing
planet = 'Pluto'
print("string5 : ",planet[0])

# Slicing
print("string5 : ",planet[-3:])

# How long is this string?
print("string5 : ",len(planet))

# Yes, we can even loop over them
print("string5 : ",[char+'! ' for char in planet])



#But a major way in which they differ from lists is that they are immutable. We can't modify them.

#planet[0] = 'B'
# planet.append doesn't work either


##String methods

# ALL CAPS
claim = "Pluto is a planet!"
print(claim.upper())

# all lowercase
print(claim.lower())

# Searching for the first index of a substring
print(claim.index('plan'))

print(claim.startswith(planet))

# false because of missing exclamation mark
print(claim.endswith('planet'))



#Going between strings and lists: .split() and .join()¶
#str.split() turns a string into a list of smaller strings, 
#breaking on whitespace by default. 
#This is super useful for taking you from one big string to a list of words.

words = claim.split()
print("words : ", words)


#Occasionally you'll want to split on something other than whitespace:
name = "Harsh-Veer-Nirwan"

first, middle, last = name.split("-")

print(first)   # Harsh
print(middle)  # Veer
print(last)    # Nirwan

#str.join() takes us in the other direction, 
# sewing a list of strings up into one long string, 
# using the string it was called on as a separator.

print("jon : ", '/'.join([first, middle, last]))

# Yes, we can put unicode characters right in our string literals :)
print(' 👏 '.join([word.upper() for word in words]))



#Building strings with .format()
#Python lets us concatenate strings with the + operator.

print(planet + ', we miss you.')

#If we want to throw in any non-string objects, 
# we have to be careful to call str() on them first


position = 9
print(planet + ", you'll always be the " + str(position) + "th planet to me.")

#This is getting hard to read and annoying to type. str.format() to the rescue.
print("{}, you'll always be the {}th planet to me.".format(planet, position))

"""
So much cleaner! We call .format() on a "format string", where the Python values we want to insert are represented with {} placeholders.

Notice how we didn't even have to call str() to convert position from an int. format() takes care of that for us.
"""

pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
#         2 decimal points   3 decimal points, format as percent     separate with commas
print("{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
    planet, pluto_mass, pluto_mass / earth_mass, population,
))



# Referring to format() arguments by index, starting from 0
s = """Pluto's a {0}.
No, it's a {1}.
{0}!
{1}!""".format('planet', 'dwarf planet')
print(s)





############## Dictionaries ###########
#this maps very directly to an Apex Map.

numbers = {
    'one': 1,
    'two': 2,
    'three': 3,
}

#In this case 'one', 'two', and 'three' are the keys, and 1, 2 and 3 are their corresponding values.

#Values are accessed via square bracket syntax similar to indexing into lists and strings.

print(numbers['one'])

#We can use the same syntax to add another key, value pair

numbers['eleven'] = 11
print(numbers)

#Or to change the value associated with an existing key
numbers['one'] = 'Pluto'
print(numbers)

#Python has dictionary comprehensions with a syntax similar to the list comprehensions
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
print(planet_to_initial)

#The in operator tells us whether something is a key in the dictionary
print('Saturn' in planet_to_initial)

#A for loop over a dictionary will loop over its keys

for k in numbers:
    print("{} = {}".format(k, numbers[k]))


#We can access a collection of all the keys or all the values with dict.keys() and dict.values(), respectively.
# Get all the initials, sort them alphabetically, and put them in a space-separated string.
print(' '.join(sorted(planet_to_initial.values())))    



#The very useful dict.items() method lets us iterate over the keys and values of a dictionary simultaneously. 
# (In Python jargon, an item refers to a key, value pair)

for planet, initial in planet_to_initial.items():
    print("{} begins with \"{}\"".format(planet.rjust(10), initial))