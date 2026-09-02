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

