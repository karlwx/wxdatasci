"""
Python Tutorial 7: NetCDF, 2D Plotting, and CartoPy

This tutorial walks through the basics of opening a netCDF (network Common Data Form) file and 
plotting some fields within a netCDF file. netCDF is a binary file format that is commonly used 
for large, 4D meteorological datasets and their associated metadata (i.e., information about the 
data such as units, location data was measured, time data was measured, instruments used, etc.).
netCDF is used almost exclusively by meteorologists and is developed at Unidata, which falls under
the umbrella of UCAR. You will likely encounter this file type in your future meteorological 
careers!

Shawn Murdzek
sfm5282@psu.edu
"""

#---------------------------------------------------------------------------------------------------
# Import Modules
#---------------------------------------------------------------------------------------------------

import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt

import cartopy.crs as ccrs
import cartopy.feature as cfeature


#---------------------------------------------------------------------------------------------------
# Opening a netCDF File
#---------------------------------------------------------------------------------------------------

# Unlike text files and other files in ASCII format, you cannot open a netCDF file using vim (try 
# it, you just get a bunch of random characters). Therefore, it is hard to visualize what is in a 
# netCDF file. To get an idea of what a netCDF file contains, use the `ncdump` command in the Linux
# terminal using the -h option (-h stands for "header").

# Try the ncdump command on the sample netCDF file tos_O1_2001-2002.nc by typing the following 
# command into the terminal:

# ncdump -h tos_O1_2001-2002.nc

# We can see that this netCDF file contains sea surface temperatures (which are saved in the field
# tos) and that tos has three dimensions: time, latitude, and longitude. We can also see that
# time is defined as days since January 1, 2001, latitude is in degrees north, longitude is in
# degrees east, and sea surface temperatures are in Kelvin. 

# Now, let's open the netCDF file in Python using the netCDF4 module:

sst_file = nc.Dataset('tos_O1_2001-2002.nc', 'r')


#---------------------------------------------------------------------------------------------------
# Extracting Fields from a netCDF File
#---------------------------------------------------------------------------------------------------

# Let's extract sea surface temperatures for the northern hemisphere from -180 deg E to 0 deg E
# (this is the part of the world that contains North America) 165 days after Jan 1, 2001. First, we
# need to determine what time, latitude, and longitude indices correspond to this domain.

# To determine the time index that corresponds to 165 days after 1 Jan 2001, we can look at the
# time field in the netCDF file. Note that sst_file.variables['time'][:] returns a NumPy array
# that we can index like any other NumPy array.

print(sst_file.variables['time'][:])

# We can see that 165 days after 1 Jan 2001 corresponds to index number 5. Let's check just to be
# sure:

time_ind = 5
print(sst_file.variables['time'][time_ind])
print()

# Now we want all latitude indices corresponding to the northern hemisphere. These will be the 
# indices corresponding to positive latitudes (negative latitudes occur in the southern 
# hemisphere!)

print(sst_file.variables['lat'][:])

# We can use the np.where function to find the indices where the latitude values are positive

lat_inds = np.where(sst_file.variables['lat'][:] > 0)[0]
lats = sst_file.variables['lat'][lat_inds]
print(lats)
print()

# Finally, we can find the indices that correspond to the longitude values between -180 and 0
# deg E. This is also equivalent to all longitude values greater than 180 deg E.

lon_inds = np.where(sst_file.variables['lon'][:] > 180.0)[0]
lons = sst_file.variables['lon'][lon_inds]
print(lons)
print()

# Now that we have our indices, we can extract the desired sea surface temperatures from the tos
# field

sst = sst_file.variables['tos'][time_ind, lat_inds, lon_inds]
print(sst)
print()


#---------------------------------------------------------------------------------------------------
# Plotting 2D Data onto a Map
#---------------------------------------------------------------------------------------------------

# Now that we have a 2D array of sea surface temperatures, let's plot these values onto a map. To
# do this, we will use the CartoPy module  

# First, we need to set up the figure and add a single axes to the figure. In the past, we used the
# function plt.subplots to create several axes on one figure (each subplot is an axes object in
# Python). Now, we will use the fig.add_subplot method to add a single axes to the figure. The
# reason for doing this is because CartoPy only works with axes objects in Python, not figure 
# objects. 

# In the fig.add_subplot method, the first argument is the the same as nrows in plt.subplots, the
# second argument is ncols (also the same as plt.subplots), and the third argument is the axes
# number we are working with (in this case, we only have one axes). The projection keyword argument
# specifies the map projection we wish to plot our data on. Other map projections offered by 
# CartoPy can be found here:
# https://scitools.org.uk/cartopy/docs/v0.15/crs/projections.html#cartopy-projections

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

# Second, we will plot the sea surface temperatures using the pcolormesh function. In order to use
# this function, we need arrays of x and y values (which in our case are longitudes and latitudes,
# respectively) that are the same shape as the sea surface temperature array. Currently, lats and 
# lons are 1D whereas sst is 2D. To make lats and lons 2D, we will use the np.meshgrid function. 

lons, lats = np.meshgrid(lons, lats)

# Now we can plot sea surface temperatures using the pcolormesh function. pcolormesh creates a 
# filled contour plot, and Python has many colormaps that can be used to color this filled
# contour plot. We can specify the colormap we wish to use with the cmap keyword. Other available
# colormaps can be found here:
# https://matplotlib.org/examples/color/colormaps_reference.html

cax = ax.pcolormesh(lons, lats, sst, cmap='plasma')

# Third, we will set the plotting domain using the set_extent method. This is similar to set_xlim
# and set_ylim, but is unique to CartoPy maps. In this case, the syntax is 
# ax.set_extent([lon_min, lon_max, lat_min, lat_max]) 

ax.set_extent([-180.0, 0.0, 0.0, 90.0])

# Fourth, we will add coastlines and country borders to our map. CartoPy has several built-in map
# features that can be added using the ax.add_feature method. Some other options include
# cfeature.LAKES for lakes and cfeature.RIVERS for rivers. 

#ax.add_feature(cfeature.COASTLINE)
#ax.add_feature(cfeature.BORDERS)

# Fifth, we will add a colorbar for the sea surface temperatures. This is done using the 
# plt.colorbar function. The first argument specifies what field the colorbar applies to (in this
# case, we want a colorbar that matches the pcolormesh function call above, which we labeled as 
# cax). We will also use the orientation keyword to make the colorbar horizontal. The set_label
# method can then be used to add a label to this colorbar.

cbar = plt.colorbar(cax, orientation='horizontal')
cbar.set_label('Sea Surface Temperature (K)', size=12)

# Finally, we will add a title and show the plot

plt.title('Sea Surface Temperatures on June 14, 2001', size=18)

plt.show()


"""
End tutorial7_netcdf_2d_plots.py
"""
