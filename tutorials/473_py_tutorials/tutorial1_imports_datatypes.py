"""
Python Tutorial: Imports and Data Types

Adapted from METEO 473 Bootcamp in Fall 2016

Shawn Murdzek
sfm5282@psu.edu
"""

#---------------------------------------------------------------------------------------------------
# Comments
#---------------------------------------------------------------------------------------------------

# Comments are chunks of text within a computer program that tell anyone reading the program what
# is going on. Thus, comments are for the human user, not the computer. It is considered good
# computer programming practice to include comments in you code so others can follow what you are
# doing.

# There are two ways of writing comments in Python:
#     Starting a line with a # makes that line a comment
#     Any lines between triple quotes (''' or """) are comments (this is referred to as a block 
#         comment)


#---------------------------------------------------------------------------------------------------
# Importing Modules
#---------------------------------------------------------------------------------------------------

# Python has limited functionality on its own, so other modules are often loaded at the beginning of
# every python program (aka "script"). A "module" is a single python file imported with
# a single import statement while a "package" (or "library") is a collection of modules.

# The numeric python package (called "numpy") is imported below. Numpy is imported with an alias, 
# which means that numpy can be referred to using its alias ("np") in the program.

import numpy as np


#---------------------------------------------------------------------------------------------------
# Python Numeric Datatypes
#---------------------------------------------------------------------------------------------------

# Integer. This type is used automatically if no decimal point is included.
# Two integers are defined below, one implicitly and the other explicitly using the "int" function.
# Note: The "type" function returns the datatype of a variable

i = 1
j = int(2.0)
print(type(i))
print(type(j))

# Float. This is a number with a decimal point

x = 2.3
y = float(1)
print(type(x))
print(type(y))

# Complex numbers. These numbers have real and imaginary parts. j is used to represent the square
# root of -1 in Python.

c = complex(1.0, 1.5)
print(c)
print(type(c))

print()


#---------------------------------------------------------------------------------------------------
# Python Boolean Datatypes
#---------------------------------------------------------------------------------------------------

# Boolean datatypes can take on two values: True (1) or False (0)

isTrue1 = bool(0)
print(isTrue1)

isTrue2 = bool(1)
print(isTrue2)

print()


#---------------------------------------------------------------------------------------------------
# Python Strings Datatypes
#---------------------------------------------------------------------------------------------------

# Strings refer to series of characters (aka text). Strings are denoted using single or double
# quotes.

name = "Shawn"
school = 'Penn State'
print(name)
print(school)
print(type(name))

# Numeric datatypes can be turned into strings using the "str" function

age = 21.6
print(type(str(age)))

# And strings can be converted into numbers too

year = '2019'
print(type(int(year)))

# Strings can be concatenated (aka combined) using "+"

print(name + " Murdzek")
print("Age = " + str(age))

# Individual characters within a string can also be selected using square brackets. Note that the
# 0 index refers to the first value!

print(name[0])
print(name[2])

# Multiple characters can be selected using the colon. For example, string[n:m] will return all
# characters between the nth and mth character in string, including the nth character but not
# including the mth character. 

print(name[1:4])

print()


#---------------------------------------------------------------------------------------------------
# Python List and Tuple Datatypes
#---------------------------------------------------------------------------------------------------

# A list is a series of objects in Python. "Objects" refer to just about anything in Python, such as
# integers, floats, complex numbers, booleans, strings, and even other lists

userList = [0, 1, 2, 3, 4, 5]
print(userList)

userList2 = [1, "hi", 2.5, 1.0+1.5j]
print(userList2)

# Items can be added to lists using "append"

userList2.append("bye")
print(userList2)

# Items in lists can also be referenced using square brackets (note that the first item in a list is
# denoted with a 0!). This is referred to as "slicing". Note how this is similar to selecting
# individual characters or groups of characters within a string.

print(userList2[1])
print(userList2[0])
print(userList2[-2])
print(userList2[1:4])
print(userList2[:2])
print(userList2[2:])

# Square brackets can also be used to delete or reassign items in a list

del userList2[4]
print(userList2)

userList2[-1] = "mymy"
print(userList2)

# Tuples are similar to lists, but unlike lists, one cannot delete, append, or reassign items within
# a tuple. Tuples are defined using parenthesis.

userTuple = (2, 1, 5)

# Tuples can be sliced like a list

print(userTuple[:2]) 

print()


#---------------------------------------------------------------------------------------------------
# Python Dictionary Datatypes
#---------------------------------------------------------------------------------------------------

# Dictionaries are similar to databases where each "key" is matched with a "value". Similarly to
# lists, "keys" and "values" can be any kind of Python object

userSFM = {"firstname": "Shawn", "lastname": "Murdzek", "age": 21.6, "Height": 70}
print(userSFM)
print(userSFM.keys())

# A value in a dictionary can be referenced using square brackets and the associated key

print(userSFM["lastname"])

print()


#---------------------------------------------------------------------------------------------------
# Numpy Numeric Datatypes
#---------------------------------------------------------------------------------------------------

# Integers and floats can also be defined using numpy, but these functions allow the user to specify
# the size of the datatype. For example, "int16" is a 16-bit (or 2-byte) integer.

i = np.int8(1)
print(i.itemsize)

j = np.int16(1)
print(j.itemsize)

x = np.float16(1)
print(x.itemsize)

y = np.float64(1)
print(y.itemsize)

print()


#---------------------------------------------------------------------------------------------------
# Numpy Arrays
#---------------------------------------------------------------------------------------------------

# Similarly to math, arrays are structured sets of numbers. Arrays in Python can be defined in
# several ways:

x = np.array([2.0, 5.8, 6.2])
print(x)

y = np.zeros(3)
print(y)

z = np.ones(4)
print(z)

# The datatype of numbers within a numpy array can be specified using the dtype keyword. Keyword
# arguments differ from regular arguments in that they are specifed using an equals sign. For 
# instance, in the function call x = np.zeros(3, dtype=int), the argument is "3" while the keyword 
# argument, "dtype", is set to "int" (which is the integer datatype).

ints = np.ones(5, dtype=int)
print(ints)                         

# np.arange and np.linspace can be used to create arrays of consecutive numbers. 
# np.arange(n) returns an array of integers from 0 to n-1
# np.arange(start, stop, step) returns an array of numbers from start to stop (but not including
# stop) at the interval step
# np.linspace(start, stop, n) returns an array of n equally spaced values between start and stop

A = np.arange(6)
print(A)

B = np.arange(3.2, 3.7, 0.1)
print(B)

C = np.linspace(2, 3, 10)
print(C)

# Numpy arrays can also have more than one dimension

a = np.array([[2.6, 5.4, 1], [3, 9, 18.5]])
print(a)

b = np.zeros([3, 4])
print(b)

# Similarly to lists, individual values or subsets of values within an array can be selected using
# square brackets ("slicing"). For 2D arrays, the syntax for slicing is [row, col]. As with lists,
# note that the first item is indexed with a 0, not a 1

print(a[1, 0])
print(a[:, 1])


"""
End tutorial1_imports_datatypes.py
"""
