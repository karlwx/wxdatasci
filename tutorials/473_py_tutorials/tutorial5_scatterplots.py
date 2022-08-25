"""
Python Tutorial: Making Scatterplots

Adapted from METEO 473 Bootcamp in Fall 2016

Shawn Murdzek
sfm5282@psu.edu
"""

#---------------------------------------------------------------------------------------------------
# Import Modules
#---------------------------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt


#---------------------------------------------------------------------------------------------------
# Basic Scatterplot
#---------------------------------------------------------------------------------------------------

# Define some data to plot

x = np.arange(-5, 6)
y = (x ** 2.0) - 5.0

# Create a figure using matplotlib.pyplot

fig = plt.figure()

# Plot the data using the matplotlib.pyplot.plot function.

plt.plot(x, y)

# Finally, show the plot in a pop-up window. You will need to close the plot to continue running
# the code!

plt.show()


#---------------------------------------------------------------------------------------------------
# Customizing Plots
#---------------------------------------------------------------------------------------------------

fig2 = plt.figure()

# This time, we will add a format string as a third argument to plot the data as a dashed red line 
# ('r--'). Other format strings that control the line color and type can be found online at
# https://matplotlib.org/2.1.1/api/_as_gen/matplotlib.pyplot.plot.html

plt.plot(x, y, 'r--')

# Add title and axes labels. The size keyword controls the font size of the title and labels.

plt.title('Quadratic Function', size=20)

plt.xlabel('x values', size=12)
plt.ylabel('y values', size=12)

# Set the x-axis limits from -6 to 6 and the y-axis limits from -10 to 30.

plt.xlim(-6, 6)
plt.ylim(-10, 30)

# Show the plot

plt.show()


#---------------------------------------------------------------------------------------------------
# Multiple Plots on a Single Figure
#---------------------------------------------------------------------------------------------------

# Create a figure and axes array. Each element in the axes array is an axes object, which represents
# a single subplot in the figure. The "figsize" keyword controls the size of the figure.

fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(9, 9))

# The syntax for plotting data onto an axes object differs slightly from plotting on a figure 
# without any axes. When in doubt, use the same function, but add the prefix "set_".

ax[0, 0].plot(x, x, 'b--')
ax[0, 0].set_title('Linear Function')
ax[0, 0].set_xlim(-6, 6)
ax[0, 0].set_ylim(-6, 6)

ax[0, 1].plot(x, x ** 2.0, 'r-')
ax[0, 1].set_title('Quadratic Function')
ax[0, 1].set_xlim(-6, 6)
ax[0, 1].set_ylim(-5, 30)

ax[1, 0].plot(x, x ** 3.0, 'g-.')
ax[1, 0].set_title('Cubic Function')
ax[1, 0].set_xlim(-6, 6)
ax[1, 0].set_ylim(-130, 130)

ax[1, 1].plot(x, x ** 4.0, 'c:')
ax[1, 1].set_title('Quartic Function')
ax[1, 1].set_xlim(-6, 6)
ax[1, 1].set_ylim(-5, 650)

# Add a title to the entire figure

plt.suptitle('Various Functions', size=20)

# Show the plot

plt.show()


"""
End tutorial5_scatterplots.py
""" 
