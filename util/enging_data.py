import os

import numpy as np
import pandas as pd
import xarray as xr

# print(os.getcwd())
# print(os.path.dirname(os.path.abspath(__file__)))
fpath = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(fpath, '../', 'Engine', 'examples', 'Engine2.Input.nc')

# xarray Dataset, define
ds = xr.Dataset(
    attrs={
        # meta
        'version':          'v0',                       # The version of this template NetCDF is 'v0', major release number of Github & Pypi
        'standard':         'WaterAccounting',          # This version applies standard of 'WaterAccounting'
        # to
        'engine':           '2',                        # The data is created for engine '2'
        'name':             'Hyperloop',                # This engine name is 'Hyperloop'
        'type':             'input',                    # This data is used as 'input' for engine2
        # from
        'created':          'WaterPix',                 # This data is created by 'WaterPix'
        'time':             '2019-12-03'                # This data is created at 'yyyy-mm-dd'
    },
    coords={
        'longitude':        [10, 20, 30],               # longitude,    np.float32
        'latitude':         [10, 20, 30, 40],           # latitude,     np.float32
        'time':             pd.date_range('2000-01-01', # time,         datetime64
                                          periods=5,
                                          freq='6H')
    },
    data_vars={
        'pcp': (                                        # name          string
            ('time', 'latitude', 'longitude'),          # dimensions    tuple
            np.random.rand(5, 4, 3)                     # values        np.ndarray
        )
    }
)

# xarray Dataset, write to NetCDF file
ds.to_netcdf(
    file,
    mode='w',
    format='NETCDF4',
    engine='netcdf4',
    encoding={
        'longitude': {
            'dtype':        np.float32
        },
        'latitude': {
            'dtype':        np.float32
        },
        'pcp': {
            'dtype':        np.float32,
            '_FillValue':   np.nan,
            'scale_factor': np.float32(1.0),
            'add_offset':   np.float32(0.0)
        }
    }
)

# xarray Dataset, open from NetCDF file
with xr.open_dataset(file) as ds:
    print(ds)
    # print(ds.keys())
