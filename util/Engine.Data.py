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
        'version':      'v0',                               # The version of this template NetCDF is 'v0', major release number of Github & Pypi
        'standard':     'WaterAccounting',                  # This version applies standard of 'WaterAccounting'
        # to
        'engine':       '2',                                # The data is created for engine '2'
        'name':         'Hyperloop',                        # This engine name is 'Hyperloop'
        'type':         'input',                            # This data is used as 'input' for engine2
        # from
        'created':      'WaterPix',                         # This data is created by 'WaterPix'
        'time':         '2019-12-03'                        # This data is created at 'yyyy-mm-dd'
    },
    coords={                                                # GTiff array,  [North, West] to [South, East]
                                                            # GTiff Origin, [West, North]
                                                            # GTiff Extent, [West, South] to [East, North] 
                                                            #               pixelWidth   = 10
                                                            #               pixelHeight  = -10
        'longitude':    (                                   # longitude,    np.ndarray
                            ['y', 'x'],
                            np.array(
                                [
                                    [0, 10],
                                    [0, 10],
                                    [0, 10]
                                ],
                                dtype=np.float32
                            )
                        ),
        'latitude':     (                                   # latitude,     np.ndarray
                            ['y', 'x'],
                            np.array(
                                [
                                    [20, 20],
                                    [10, 10],
                                    [0,  0]
                                ],
                                dtype=np.float32
                            )
                        ),
        'time':         pd.date_range('2000-01-01',         # time,         datetime64
                                      periods=2,
                                      freq='D')
    },
    data_vars={
        'pcp': (                                            # variable,     dims,val,attr,encoding
                        (                                   # dimensions,   tuple
                            'time',
                            'y',
                            'x'
                        ),
                        np.array(                           # values,       np.ndarray
                            [
                                [
                                    [1, 2],
                                    [3, 4],
                                    [5, 6]
                                ],
                                [
                                    [10, 20],
                                    [30, 40],
                                    [50, 60]
                                ]
                            ],
                            dtype=np.float32
                        ),
                        {                                   # attributes,   dict
                            'units':        'mm/day'
                        },
                        {                                   # encoding,     dict
                            'dtype':        np.float32,
                            '_FillValue':   np.nan,
                            'scale_factor': np.float32(1.0),
                            'add_offset':   np.float32(0.0)
                        }
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
            'dtype':    np.float32
        },
        'latitude': {
            'dtype':    np.float32
        }
    }
)

# xarray Dataset, open from NetCDF file
with xr.open_dataset(file) as ds:
    print(ds)
    # print(ds.keys())
