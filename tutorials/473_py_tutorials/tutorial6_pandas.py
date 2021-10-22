"""
Python Tutorial: Pandas

Pandas is a Python data analysis library that has similar functionality to Excel and SQLite. The
goal of this tutorial is to get our feet wet with Pandas and demonstrate some of the functions in
Pandas that I find to be the most helpful. To learn more about Pandas, use the official 
documentation (https://pandas.pydata.org/) or Google your specific question.

Shawn Murdzek
sfm5282@psu.edu
"""

#---------------------------------------------------------------------------------------------------
# Import Modules
#---------------------------------------------------------------------------------------------------

import pandas as pd


#---------------------------------------------------------------------------------------------------
# Read in a CSV File
#---------------------------------------------------------------------------------------------------

# We will use the file mm_data for this tutorial, which contains observations from a mobile mesonet
# probe during VORTEX2. The contents of this file are as follows:
#     time = Time in decimal hours
#     lat = Latitude in degrees north
#     lon = Longitude in degrees west
#     T = Temperature in deg C
#     RH = Relative humidity in %
#     p = Pressure in mb
#     dir = Direction wind is blowing to, in degrees from north
#     spd = Wind speed in m/s
#     qc = Quality control flag (1 = problem with wind data, 0 = no problem)

# mm_data is a csv file. CSV stands for "comma-separated-values" and is a type of text file that 
# has data stored in an orderly fashion, often separated by commas or spaces. The file mm_data is 
# an example of a CSV. Feel free to open this file using a text editor in order to examine the 
# structure of the file.

# We could read in mm_data using the open and readline functions, but this would require us to 
# manually separate the different values in each line and place them into separate arrays (this is
# often referred to as "parsing" data). Using Pandas, we can read in the csv and place the data into 
# a Pandas object called a "DataFrame" using a single command. 

mm_df = pd.read_csv('mm_data', delim_whitespace=True)

# Additional documentation on this function, including what to do if headers are not included in the
# csv, is found here https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html
# Note: Pandas can read several other file types other than CSV files, including Excel files.


#---------------------------------------------------------------------------------------------------
# Slicing DataFrames
#---------------------------------------------------------------------------------------------------

# To get an idea of what a DataFrame looks like, let's start by printing the DataFrame. Note how the
# structure is similar to that of an Excel spreadsheet

print(mm_df)
print()

# Now let's select certain columns (which are called "Series" in Pandas) in the DataFrame using 
# the series names

print(mm_df['T'])
print()

print(mm_df['RH'][:10])
print()

# We can also only select rows where a certain condition is true using the loc attribute. Here we 
# only select the rows where qc is set to 0.

print(mm_df.loc[mm_df['qc'] == 0])
print()


#---------------------------------------------------------------------------------------------------
# Basic Computations in Pandas
#---------------------------------------------------------------------------------------------------

# Many computations such as mean, maximum, minimum, standard deviation, etc. can be performed in
# Pandas. Note how for the relative humidity, a double percent sign is needed, otherwise Python
# interprets % as a string formatting operator.

print('Mean Temperature = %.2f deg C' % mm_df['T'].mean())
print('Maximum Relative Humidity = %.2f %%' % mm_df['RH'].max())
print('Standard Deviation of Wind Speed = %.2f m/s' % mm_df['spd'].std())
print()


#---------------------------------------------------------------------------------------------------
# Adding New Series to a DataFrame
#---------------------------------------------------------------------------------------------------

# New series (columns) can be added to a Pandas DataFrame. For example, we might want another series
# for potential temperature (theta) in Kelvin. We can define this new series using the existing
# temperature and pressure series

mm_df['theta'] = (mm_df['T'] + 273.15) * ((1000.0 / mm_df['p']) ** (287.04 / 1005.0))

print(mm_df[:10])
print()


#---------------------------------------------------------------------------------------------------
# Converting to Numpy Arrays
#---------------------------------------------------------------------------------------------------

# Individual series in a DataFrame can be converted to 1D numpy arrays using the values attribute

T = mm_df['T'].values

print(type(T))


"""
End tutorial6_pandas.py
"""