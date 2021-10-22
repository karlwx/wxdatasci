"""
Python Tutorial: Calling a User-Defined Function

Adapted from METEO 473 Bootcamp in Fall 2016

Shawn Murdzek
sfm5282@psu.edu
"""

#---------------------------------------------------------------------------------------------------
# Import the File Containing the Function We Created
#---------------------------------------------------------------------------------------------------

import tutorial4_1_def_fct as df


#---------------------------------------------------------------------------------------------------
# Call Function
#---------------------------------------------------------------------------------------------------

leg1 = 12.0
leg2 = 5.0
hyp = df.right_triangle(leg1, leg2)

print('Hypotenuse = %.2f' % hyp)


"""
End tutorial4_2_fct_call.py
"""
