"""
Python Tutorial: Sample User-Defined Function

Adapted from METEO 473 Bootcamp in Fall 2016

Shawn Murdzek
sfm5282@psu.edu
"""

#---------------------------------------------------------------------------------------------------
# Import Modules
#---------------------------------------------------------------------------------------------------

import numpy as np


#---------------------------------------------------------------------------------------------------
# Define a Function
#---------------------------------------------------------------------------------------------------

# If the same chunk of code is used several times within a program, that chunk of code can be turned
# into a function in order to save space. Typically, one Python file or a series of Python files
# contain only functions and these functions are then called in a separate Python file called the
# "driver". The driver here is tutorial4_2_fct_call.py.

def right_triangle(a, b):
    """
    Returns the hypotenuse of a right triangle given the lengths of the two legs.
    Inputs:
        a = Length of the first leg
        b = Length of the second leg
    Outputs:
        c = Length of the hypotenuse
    """

    c = np.sqrt((a ** 2) + (b ** 2))

    return c


"""
End tutorial4_1_def_fct.py
"""
