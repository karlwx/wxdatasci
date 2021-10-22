"""
Python Tutorial: String Formatting and File I/O

Adapted from METEO 473 Bootcamp in Fall 2016

Shawn Murdzek
sfm5282@psu.edu
"""

#---------------------------------------------------------------------------------------------------
# String Formatting
#---------------------------------------------------------------------------------------------------

# String formatting is used to place other strings/integers/floats into an existing string using
# the % operator

print('There are %d cows' % 2)
print('A bus pass costs $%.2f' % 2.330)

# Common argument specifiers for string formatting:
#     %d is an integer
#     %.xf is a float with x decimal places
#     %s is a string

string = '%d is %s than %.3f'

ints = [2, 9, 6, 7]
floats = [3.2, 6.8, 1.2, 9.4]

for i, f in zip(ints, floats):
    if i > f:
        print(string % (i, 'greater', f))
    elif i < f:
        print(string % (i, 'less', f))

print()


#---------------------------------------------------------------------------------------------------
# File I/O
#---------------------------------------------------------------------------------------------------

# I/O is short hand for "input / output", so file I/O refers to writing and reading data from a file

# Files can be opened using the "open" function. The second argument of the "open" function is a
# string that specifies the file permissions:
#     'r' = read
#     'w' = write
#     'a' = append (add something to the end)

# Open a file. fptr is short hand for "file pointer" and is an object used to reference the opened
# file in the code.

fptr = open('test_file.txt', 'w')

# Write individual lines to the file. Use \n to go to the next line and \t to tab

fptr.write('Here is the first line\n')
fptr.write('\tHere is a tabbed line\n')

for i in range(5, 0, -1):
    fptr.write('%d...\n' % i)

fptr.write('LIFT OFF!')

# Always close files when you are done using them

fptr.close()

# Now let's read in test_file.txt

fptr = open('test_file.txt', 'r')

print(fptr.readline())

# readline() reads a single line. If we call readline() again, we will get the next line

print(fptr.readline())

# We can also read lines using a loop. Note that the first two lines are not read because we read
# them already!

for l in fptr:
    print(l)

# Return to the first line using "seek". Note that the argument of seek refers to the byte of data,
# not the line

fptr.seek(0)

# Read all the lines of fptr into a list

contents = fptr.readlines()

print("This file has %d lines" % len(contents))

# The strip function can be used to remove \n or \t

for l in contents:
    print(l.strip())

fptr.close()

# Parting thoughts about file I/O:
#
# The "open" function works well for basic text files, but in meteorology we often deal with large
# files that are in other formats (e.g. csv, xls, netcdf, grib). These formats are not handled by
# the "open" function. Luckily, there are other packages in Python that can open these types of
# files. The pandas package has several functions for I/O with csv or xls files. The NetCDF4 module
# or the scipy module can handle netcdf files. The pygrib module can handle grib files. Even more
# exotic file types, such as Level II radar data, can be handled in Python using Py-ART. If you ever
# find a file type and are not sure how to open it in Python, use Google. There is probably a module
# that can open it!


"""
End tutorial3_str_formatting_io.py
"""
