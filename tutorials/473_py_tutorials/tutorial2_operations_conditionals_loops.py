"""
Python Tutorial: Mathematical Operations, Conditional Statements, and Loops

Adapted from METEO 473 Bootcamp in Fall 2016

Shawn Murdzek
sfm5282@psu.edu
"""

#---------------------------------------------------------------------------------------------------
# Import Modules
#---------------------------------------------------------------------------------------------------

import numpy as np


#---------------------------------------------------------------------------------------------------
# Mathematical Operations
#---------------------------------------------------------------------------------------------------

x = 2.1
y = 9.0
i = int(3)
j = int(2)
A = np.array([2.0, 3.0, 5.0])
B = np.array([10.1, 9.9, 3.0])

# Rules of Thumb:
#     An operation between two integers yields an integer (with the exception of division, integer
#         division yields a float)
#     Any operations between two arrays are performed element-wise
#     Any operation involving a float yields a float

print(x + y)
print(j - i)
print(type(i + j))
print(type(i + x))

print(A - B)
print(A * B)
print(i / j)
print(y / j)

# Exponents are performed using **

print(y ** 2)
print(A ** 3)

# The remainder from a division operation can be returned using %

print(i % j)

# More complex operations can be performed using numpy
# Note that "np.log" refers to the natural logarithm (i.e. ln)

print(np.cos(np.pi / 4))
print(np.exp(10))
print(np.arcsin(0.5))
print(np.log(np.e ** 2))

print()


#---------------------------------------------------------------------------------------------------
# Conditional Statements
#---------------------------------------------------------------------------------------------------

# Conditional statements execute a block of code if the defined boolean expression is True

if 2 > 1:
    print('2 is greater than 1')
else:
    print('2 is not greater than 1')

# Note how the print statements within the conditional statement above are indented. Code this is
# not indented is not considered part of the conditional statement

x = 2.0
y = 3.0

if x > 1:
    x = x + 2
    print(x)

if x < 3:

    # Note how neither of these statements run since x is not less than 3
    
    x = x + 5
    print(x)

# Other inequalities that can be used in conditional statements include:
#     >= greater than or equal to
#     <= less than or equal to
#     == equal to

z = 5.0

if z <= 1:
    print('z is less than or equal to 1')
elif z <= 3:
    print('z is less than or equal to 3')
elif z <= 5:
    print('z is less than or equal to 5')
elif z <= 7:
    print('z is less than or equal to 7')
else:
    print('z is greater than 7')

# In the code above, note how once one of the if - else if - else statements is true, the remaining
# conditions are skipped

# More complex boolean expressions can be constructed using "and", "or", and "not"

x = 5.0
y = 2.0

if not True:
    print('False')

if (x > 3) and (y > 3):
    print('Both numbers are greater than 3')
else:
    print('One or both of these numbers are less than 3')

if (x > 3) or (y > 3):
    print('One of these numbers is greater than 3')
else:
    print('Neither of these numbers are less than 3')

print()


#---------------------------------------------------------------------------------------------------
# Loops
#---------------------------------------------------------------------------------------------------

# Similar to other programming languages, Python supports two types of loops: for loops and while
# loops

# Note how the blocks of code within each loop must be indented, just like conditional statements

print('Basic for loop')
for a in [2, 5, 'hello']:
    print(a)

x = 1

print('Basic while loop')
while x <= 5:
    x = x + 2
    print(x)

# The "range" function can be used to loop through a sequence of numbers

print('Example using range')
for a in range(5):
    print(a)

# Loops can also be nested in other loops or conditional statements

print('Nested for loop')
for i in range(2):
    for j in range(3):
        print(i, j)

A = np.array([2.2, 6.0, 7.2, 8.4, 10.0])

print('Conditional statement nested in a for loop')
for num in A:
    if num >= 7:
        print(num)


"""
End tutorial2_operations_conditionals_loops.py
"""
