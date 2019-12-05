import os

import datetime
import numpy as np
import pandas as pd
import xarray as xr

# print(os.getcwd())
# print(os.path.dirname(os.path.abspath(__file__)))
fpath = os.path.dirname(os.path.abspath(__file__))

# %% Engine2.Input.nc
file = os.path.join(fpath, '../', 'Engine', 'examples', 'Engine2.Input.nc')

# xarray Dataset, define
ds_FillValue        = np.NaN
ds_coords_dtype     = np.float32
ds_data_vars_dtype  = np.float32
ds = xr.Dataset.from_dict(
{
    'attrs': {
        # meta
        'version':      'v0',                               # The version of this template NetCDF is 'v0', major release number of Github & Pypi
        'standard':     'WaterAccounting',                  # This version applies standard of 'WaterAccounting'
        # to
        'engine':       '2',                                # The data is created for engine '2'
        'name':         'Hyperloop',                        # This engine name is 'Hyperloop'
        'type':         'input',                            # This data is used as 'input' for engine2
        # from
        'created':      'WaterPix',                         # This data is created by 'WaterPix'
        'time':         '2019-12-03',                       # This data is created at 'yyyy-mm-dd'
        # GTiff format
                                                            # GTiff Origin, [West, North]
                                                            # GTiff Extent, [West, South] to [East, North] 
                                                            #               pixelWidth   = 10
                                                            #               pixelHeight  = -10
        'CRS':          'EPSG:4326 - WGS 84 - Geographic',  # CRS name linked with variable 'crs'
        'originX':      0,                                  # West
        'originY':      20,                                 # North
        'rasterW':      10,                                 # pixel Width
        'rasterH':      -10                                 # pixel Height
    },
    'dims': {
        'time':         2,
        'y':            3,
        'x':            2
    },
    'coords': {                                             # GTiff array,  [North, West] to [South, East]
        'lon': {                                            # longitude,    np.ndarray
                'dims': ('y', 'x'),
                'attrs': {
                        'standard_name': 'longitude',
                        'units':         'degree',
                        'axis':          'Y'
                },
                'data': np.array(
                        [
                            [0, 10],
                            [0, 10],
                            [0, 10]
                        ],
                        dtype=ds_coords_dtype
                )
        },
        'lat': {                                            # latitude,    np.ndarray
                'dims': ('y', 'x'),
                'attrs': {
                        'standard_name': 'latitude',
                        'units':         'degree',
                        'axis':          'Y'
                },
                'data': np.array(
                        [
                            [20, 20],
                            [10, 10],
                            [0,  0]
                        ],
                        dtype=ds_coords_dtype
                )
        },
        'time': {
                'dims': ('time'),
                'attrs': {
                        'standard_name': 'time',
                        'long_name':     'time'
                },
                'data': np.array(
                        [
                            datetime.datetime(2000, 1, 1, 0, 0, 0),
                            datetime.datetime(2000, 1, 2, 0, 0, 0)
                        ]
                )
        }
        # 'time':         pd.date_range('2000-01-01',       # time,         datetime64
        #                               periods=2,
        #                               freq='D')
    },
    'data_vars': {
        'crs': {                                            # variable short name, 'crs': 'EPSG:4326 - WGS 84 - Geographic'
                'dims': (),
                'attrs': {
                        'standard_name':                    'CRS',
                        'long_name':                        'Coordinate Reference System',
                        'grid_mapping_name':                'latitude_longitude',
                        
                        'spatial_ref':                      'GEOGCS[\"GCS_WGS_1984\",DATUM[\"WGS_1984\",SPHEROID[\"WGS_84\",6378137.0,298.257223563]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.017453292519943295]]',
                        'longitude_of_prime_meridian':      0.0,
                        'semi_major_axis':                  6378137.0,
                        'inverse_flattening':               298.257223563
                },
                'data': ds_FillValue
        },
        'pcp': {                                            # variable short name
                'dims': (                                   # variable dimensions
                        'time',
                        'y',
                        'x'
                ),
                'attrs': {                                  # variable attributes
                                                            # 'grid_mapping' linked with variable 'crs'
                        'grid_mapping':  'crs',
                        'standard_name': 'precipitation',
                        'long_name':     'precipitation',
                        'units':         'mm/day'
                },
                'data': np.array(                           # variable data, np.array(, dtype=)
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
                        dtype=ds_data_vars_dtype
                )
        },
        'pet': {
                'dims': ('time', 'y', 'x'),
                'attrs': {
                        'standard_name': 'potential evapotranspiration',
                        'long_name':     'potential evapotranspiration',
                        'units':         'mm/day',
                        'grid_mapping':  'crs'
                },
                'data': np.array(
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
                        dtype=ds_data_vars_dtype
                )
        }
    }
})

# xarray Dataset, write to NetCDF file
ds.to_netcdf(
    file,
    mode='w',
    format='NETCDF4',
    engine='netcdf4',
    encoding={
        # coord
        'lon': {
            'dtype':        ds_coords_dtype
        },
        'lat': {
            'dtype':        ds_coords_dtype
        },
        # data_vars
        'crs': {
            'dtype':        ds_data_vars_dtype
        },
        'pcp': {
            'dtype':        ds_data_vars_dtype,
            '_FillValue':   ds_FillValue,
            'scale_factor': ds_data_vars_dtype(1.0),
            'add_offset':   ds_data_vars_dtype(0.0)
        },
        'pet': {
            'dtype':        ds_data_vars_dtype,
            '_FillValue':   ds_FillValue,
            'scale_factor': ds_data_vars_dtype(1.0),
            'add_offset':   ds_data_vars_dtype(0.0)
        }
    }
)

# xarray Dataset, close NetCDF file
ds.close()

# xarray Dataset, open from NetCDF file
with xr.open_dataset(file) as ds:
    print(ds)
    # print(ds.keys())
