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
