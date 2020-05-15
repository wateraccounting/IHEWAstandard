# %% [markdown]
# # Writing netCDF data
# 
# **Important Note**: when running this notebook interactively in a browser, you probably will not be able to execute individual cells out of order without getting an error.  Instead, choose "Run All" from the Cell menu after you modify a cell.

# %%
import os

import netCDF4     # Note: python is case-sensitive!
import numpy as np

fpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../', 'Data', 'examples')

# %% [markdown]
# ## Opening a file, creating a new Dataset
# 
# Let's create a new, empty netCDF file named 'NetCDF-new1.nc', opened for writing.
# 
# Be careful, opening a file with 'w' will clobber any existing data (unless `clobber=False` is used, in which case an exception is raised if the file already exists).
# 
# - `mode='r'` is the default.
# - `mode='a'` opens an existing file and allows for appending (does not clobber existing data)
# - `format` can be one of `NETCDF3_CLASSIC`, `NETCDF3_64BIT`, `NETCDF4_CLASSIC` or `NETCDF4` (default). `NETCDF4_CLASSIC` uses HDF5 for the underlying storage layer (as does `NETCDF4`) but enforces the classic netCDF 3 data model so data can be read with older clients.  

# %%
try: 
    ncfile.close()  # just to be safe, make sure dataset is not already open.
except: 
    pass

ncfile = netCDF4.Dataset(os.path.join(fpath, 'NetCDF.Single.nc'),mode='w',format='NETCDF4_CLASSIC') 
print(ncfile)

# %% [markdown]
# ## Creating dimensions
# 
# The **ncfile** object we created is a container for _dimensions_, _variables_, and _attributes_.   First, let's create some dimensions using the [`createDimension`](http://unidata.github.io/netcdf4-python/netCDF4.Dataset-class.html#createDimension) method.  
# 
# - Every dimension has a name and a length.  
# - The name is a string that is used to specify the dimension to be used when creating a variable, and as a key to access the dimension object in the `ncfile.dimensions` dictionary.
# 
# Setting the dimension length to `0` or `None` makes it unlimited, so it can grow. 
# 
# - For `NETCDF4` files, any variable's dimension can be unlimited.  
# - For `NETCDF4_CLASSIC` and `NETCDF3*` files, only one per variable can be unlimited, and it must be the leftmost (fastest varying) dimension.

# %%
lat_dim = ncfile.createDimension('lat', 73)     # latitude axis
lon_dim = ncfile.createDimension('lon', 144)    # longitude axis
time_dim = ncfile.createDimension('time', None) # unlimited axis (can be appended to).

for dim in ncfile.dimensions.items():
    print(dim)

# %% [markdown]
# ## Creating attributes
# 
# netCDF attributes can be created just like you would for any python object. 
# 
# - Best to adhere to established conventions (like the [CF](http://cfconventions.org/) conventions)
# - We won't try to adhere to any specific convention here though.

# %%
ncfile.title='My model data'
print(ncfile.title)

# %% [markdown]
# Try adding some more attributes...
# %% [markdown]
# ## Creating variables
# 
# Now let's add some variables and store some data in them.  
# 
# - A variable has a name, a type, a shape, and some data values.  
# - The shape of a variable is specified by a tuple of dimension names.  
# - A variable should also have some named attributes, such as 'units', that describe the data.
# 
# The [`createVariable`](http://unidata.github.io/netcdf4-python/netCDF4.Dataset-class.html#createVariable) method takes 3 mandatory args.
# 
# - the 1st argument is the variable name (a string). This is used as the key to access the variable object from the `variables` dictionary.
# - the 2nd argument is the datatype (most numpy datatypes supported).  
# - the third argument is a tuple containing the dimension names (the dimensions must be created first).  Unless this is a `NETCDF4` file, any unlimited dimension must be the leftmost one.
# - there are lots of optional arguments (many of which are only relevant when `format='NETCDF4'`) to control compression, chunking, fill_value, etc.
# 

# %%
# Define two variables with the same names as dimensions,
# a conventional way to define "coordinate variables".
lat = ncfile.createVariable('lat', np.float32, ('lat',))
lat.units = 'degrees_north'
lat.long_name = 'latitude'

lon = ncfile.createVariable('lon', np.float32, ('lon',))
lon.units = 'degrees_east'
lon.long_name = 'longitude'

time = ncfile.createVariable('time', np.float64, ('time',))
time.units = 'hours since 1800-01-01'
time.long_name = 'time'

# Define a 3D variable to hold the data
temp = ncfile.createVariable('temp',np.float64,('time','lat','lon')) # note: unlimited dimension is leftmost
temp.units = 'K' # degrees Kelvin
temp.standard_name = 'air_temperature' # this is a CF standard name
print(temp)

# %% [markdown]
# ## Pre-defined variable attributes (read only)
# 
# The netCDF4 module provides some useful pre-defined Python attributes for netCDF variables, such as dimensions, shape, dtype, ndim. 
# 
# Note: since no data has been written yet, the length of the 'time' dimension is 0.

# %%
print("-- Some pre-defined attributes for variable temp:")
print("temp.dimensions:", temp.dimensions)
print("temp.shape:", temp.shape)
print("temp.dtype:", temp.dtype)
print("temp.ndim:", temp.ndim)

# %% [markdown]
# ## Writing data
# 
# To write data to a netCDF variable object, just treat it like a numpy array and assign values to a slice.

# %%
nlats = len(lat_dim); nlons = len(lon_dim); ntimes = 3

# Write latitudes, longitudes.
# Note: the ":" is necessary in these "write" statements
lat[:] = -90. + (180./nlats)*np.arange(nlats) # south pole to north pole
lon[:] = (180./nlats)*np.arange(nlons) # Greenwich meridian eastward

# create a 3D array of random numbers
data_arr = np.random.uniform(low=280,high=330,size=(ntimes,nlats,nlons))

# Write the data.  This writes the whole 3D netCDF variable all at once.
temp[:,:,:] = data_arr  # Appends data along unlimited dimension
print("-- Wrote data, temp.shape is now ", temp.shape)
# read data back from variable (by slicing it), print min and max
print("-- Min/Max values:", temp[:,:,:].min(), temp[:,:,:].max())

# %% [markdown]
# - You can just treat a netCDF Variable object like a numpy array and assign values to it.
# - Variables automatically grow along unlimited dimensions (unlike numpy arrays)
# - The above writes the whole 3D variable all at once,  but you can write it a slice at a time instead.
# 
# Let's add another time slice....
# 

# %%
# create a 2D array of random numbers
data_slice = np.random.uniform(low=280,high=330,size=(nlats,nlons))

# Append the data.  This appends the 2D netCDF variable at the end along the dimension.
temp[3,:,:] = data_slice   # Appends the 4th time slice
print("-- Wrote more data, temp.shape is now ", temp.shape)

# %% [markdown]
# Note that we have not yet written any data to the time variable.  It automatically grew as we appended data along the time dimension to the variable `temp`, but the data is missing.

# %%
print(time)
times_arr = time[:]
print(type(times_arr),times_arr)  # dashes indicate masked values (where data has not yet been written)

# %% [markdown]
# Let's add write some data into the time variable.  
# 
# - Given a set of datetime instances, use date2num to convert to numeric time values and then write that data to the variable.

# %%
from datetime import datetime
from netCDF4 import date2num,num2date

# 1st 4 days of October.
dates = [datetime(2014,10,1,0),datetime(2014,10,2,0),datetime(2014,10,3,0),datetime(2014,10,4,0)]
print(dates)

times = date2num(dates, time.units)
print(times, time.units) # numeric values

time[:] = times
# read time data back, convert to datetime instances, check values.
print(num2date(time[:],time.units))

# %% [markdown]
# ## Closing a netCDF file
# 
# It's **important** to close a netCDF file you opened for writing:
# 
# - flushes buffers to make sure all data gets written
# - releases memory resources used by open netCDF files

# %%
# first print the Dataset object to see what we've got
print(ncfile)
# close the Dataset.
ncfile.close(); print('Dataset is closed!')

# %% [markdown]
# # Advanced features
# 
# So far we've only exercised features associated with the old netCDF version 3 data model.  netCDF version 4 adds a lot of new functionality that comes with the more flexible HDF5 storage layer.  
# 
# Let's create a new file with `format='NETCDF4'` so we can try out some of these features.

# %%
ncfile = netCDF4.Dataset(os.path.join(fpath, 'NetCDF.Group.nc'),'w',format='NETCDF4')
print(ncfile)

# %% [markdown]
# ## Creating Groups
# 
# netCDF version 4 added support for organizing data in hierarchical groups.
# 
# - analagous to directories in a filesystem. 
# - Groups serve as containers for variables, dimensions and attributes, as well as other groups. 
# - A `netCDF4.Dataset` creates a special group, called the 'root group', which is similar to the root directory in a unix filesystem. 
# 
# - groups are created using the [`createGroup`](http://unidata.github.io/netcdf4-python/netCDF4.Dataset-class.html#createGroup) method.
# - takes a single argument (a string, which is the name of the Group instance).  This string is used as a key to access the group instances in the `groups` dictionary.
# 
# Here we create two groups to hold data for two different model runs.

# %%
grp1 = ncfile.createGroup('model_run1')
grp2 = ncfile.createGroup('model_run2')
for grp in ncfile.groups.items():
    print(grp)

# %% [markdown]
# Create some dimensions in the root group.

# %%
lat_dim = ncfile.createDimension('lat', 73)     # latitude axis
lon_dim = ncfile.createDimension('lon', 144)    # longitude axis
time_dim = ncfile.createDimension('time', None) # unlimited axis (can be appended to).

# %% [markdown]
# Now create a variable in grp1 and grp2.  The library will search recursively upwards in the group tree to find the dimensions (which in this case are defined one level up).
# 
# - These variables are create with **zlib compression**, another nifty feature of netCDF 4. 
# - The data are automatically compressed when data is written to the file, and uncompressed when the data is read.  
# - This can really save disk space, especially when used in conjunction with the [**least_significant_digit**](http://unidata.github.io/netcdf4-python/netCDF4.Dataset-class.html#createVariable) keyword argument, which causes the data to be quantized (truncated) before compression.  This makes the compression lossy, but more efficient.

# %%
temp1 = grp1.createVariable('temp',np.float64,('time','lat','lon'),zlib=True)
temp2 = grp2.createVariable('temp',np.float64,('time','lat','lon'),zlib=True)
for grp in ncfile.groups.items():  # shows that each group now contains 1 variable
    print(grp)

# %% [markdown]
# ##Creating a variable with a compound data type
# 
# - Compound data types map directly to numpy structured (a.k.a 'record' arrays). 
# - Structured arrays are akin to C structs, or derived types in Fortran. 
# - They allow for the construction of table-like structures composed of combinations of other data types, including other compound types. 
# - Might be useful for representing multiple parameter values at each point on a grid, or at each time and space location for scattered (point) data. 
# 
# Here we create a variable with a compound data type to represent complex data (there is no native complex data type in netCDF). 
# 
# - The compound data type is created with the [`createCompoundType`](http://unidata.github.io/netcdf4-python/netCDF4.Dataset-class.html#createCompoundType) method.

# %%
# create complex128 numpy structured data type
complex128 = np.dtype([('real',np.float64),('imag',np.float64)])
# using this numpy dtype, create a netCDF compound data type object
# the string name can be used as a key to access the datatype from the cmptypes dictionary.
complex128_t = ncfile.createCompoundType(complex128,'complex128')
# create a variable with this data type, write some data to it.
cmplxvar = grp1.createVariable('cmplx_var',complex128_t,('time','lat','lon'))
# write some data to this variable
# first create some complex random data
nlats = len(lat_dim); nlons = len(lon_dim)
data_arr_cmplx = np.random.uniform(size=(nlats,nlons))+1.j*np.random.uniform(size=(nlats,nlons))
# write this complex data to a numpy complex128 structured array
data_arr = np.empty((nlats,nlons),complex128)
data_arr['real'] = data_arr_cmplx.real; data_arr['imag'] = data_arr_cmplx.imag
cmplxvar[0] = data_arr  # write the data to the variable (appending to time dimension)
print(cmplxvar)
data_out = cmplxvar[0] # read one value of data back from variable
print(data_out.dtype, data_out.shape, data_out[0,0])

# %% [markdown]
# ##Creating a variable with a variable-length (vlen) data type
# 
# netCDF 4 has support for variable-length or "ragged" arrays. These are arrays of variable length sequences having the same type. 
# 
# - To create a variable-length data type, use the [`createVLType`](http://unidata.github.io/netcdf4-python/netCDF4.Dataset-class.html#createVLType) method.
# - The numpy datatype of the variable-length sequences and the name of the new datatype must be specified. 

# %%
vlen_t = ncfile.createVLType(np.int64, 'phony_vlen')

# %% [markdown]
# A new variable can then be created using this datatype.

# %%
vlvar = grp2.createVariable('phony_vlen_var', vlen_t, ('time','lat','lon'))

# %% [markdown]
# Since there is no native vlen datatype in numpy, vlen arrays are represented in python as object arrays (arrays of dtype `object`). 
# 
# - These are arrays whose elements are Python object pointers, and can contain any type of python object. 
# - For this application, they must contain 1-D numpy arrays all of the same type but of varying length. 
# - Fill with 1-D random numpy int64 arrays of random length between 1 and 10.

# %%
vlen_data = np.empty((nlats,nlons), dtype=np.int64)
try:
    for i in range(nlons):
        for j in range(nlats):
            size = np.random.randint(1,10,size=1) # random length of sequence
            vlen_data[j,i] = np.random.randint(0,10,size=size)# generate random sequence
    vlvar[0] = vlen_data # append along unlimited dimension (time)
except:
    pass
print(vlvar)
print('data =\n',vlvar[:])

# %% [markdown]
# Close the Dataset and examine the contents with ncdump.

# %%
ncfile.close()
