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
ds_FillValue_i4  = -9999
ds_FillValue_f4  = np.NaN
ds_coords_dtype  = np.float32
ds_data_vars_i4  = np.int32
ds_data_vars_f4  = np.float32
ds = xr.Dataset.from_dict(
{
    'attrs': {
        # meta
        'version':          'v0',                           # The version of this template NetCDF is 'v0', major release number of Github & Pypi
        'standard':         'WaterAccounting',              # This version applies standard of 'WaterAccounting'
        # to
        'engine_num':       '2',                            # The data is created for engine '2'
        'engine_use':       'Input',                        # The data is used as 'input' for engine2
        'model_name':       'Hyperloop',                    # The engine model,   linked with release name
        'model_version':    'v0.0.1',                       # The engine version, linked with release version
        # from
        'created_by':       'IHE',                          # This data is created by owner 'IHE'
        'created_time':     '2019-12-03',                   # This data is created at time  'yyyy-mm-dd'
        'created_model':    'WaterPix',                     # This data is created by model 'WaterPix'
        # GTiff format
                                                            # GTiff Origin, [West, North]
                                                            # GTiff Extent, [West, South] to [East, North]
                                                            # GTiff         rasterWidth  = 10
                                                            # GTiff         rasterHeight = -10
                                                            # Image         pixelWidth   = 10
                                                            # Image         pixelHeight  = 10
                                                            # CRS name,     linked with variable 'crs'
        'CRS':              'EPSG:4326 - WGS 84 - Geographic', 
        'originX':          0.0,                            # West
        'originY':          20.0,                           # North
        'rasterW':          10.0,                           # pixel Width
        'rasterH':          -10.0                           # pixel Height
    },
    'dims': {
        'time':             2,
        'y':                3,
        'x':                2
    },
    'coords': {                                             # GTiff array,  [North, West] to [South, East]
        'lon': {                                            # longitude,    np.ndarray
                'dims': ('y', 'x'),
                'attrs': {
                        'standard_name': 'Longitude',
                        'long_name':     'Longitude',
                        'units':         'degrees_east',
                        'axis':          'x'
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
                        'standard_name': 'Latitude',
                        'long_name':     'Latitude',
                        'units':         'degrees_north',
                        'axis':          'y'
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
        'time': {                                           # time,        np.ndarray
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
        # CRS
        'crs': {                                            # variable short name, 'crs': 'EPSG:4326 - WGS 84 - Geographic'
                                                            # DO NOT CHANGE 'crs'!
                'dims': (),
                'attrs': {
                        'standard_name':                    'CRS',
                        'long_name':                        'Coordinate Reference System',
                        'grid_mapping_name':                'latitude_longitude',
                        
                        'spatial_ref':                      'GEOGCS['
                                                                'GCS_WGS_1984,'
                                                                'DATUM['
                                                                    'WGS_1984,'
                                                                    'SPHEROID['
                                                                        'WGS_84,'
                                                                        '6378137.0,'
                                                                        '298.257223563'
                                                                    ']'
                                                                '],'
                                                                'PRIMEM['
                                                                    'Greenwich,'
                                                                    '0.0'
                                                                '],'
                                                                'UNIT['
                                                                    'Degree,'
                                                                    '0.017453292519943295'
                                                                ']'
                                                            ']',
                        'longitude_of_prime_meridian':      0.0,
                        'semi_major_axis':                  6378137.0,
                        'inverse_flattening':               298.257223563
                },
                'data': ds_FillValue_f4
        },

        # # 0D
        # 'name': {
        #         'dims': (),                             # variable dimensions, 0D
        #         'attrs': {
        #                 'standard_name':    'Basin Name',
        #                 'long_name':        'Basin Name'
        #         },
        #         'data': 'VGTB'
        # },
        # 'recycling_ratio': {
        #         'dims': (),
        #         'attrs': {
        #                 'standard_name':    'Recycling Ratio',
        #                 'long_name':        'Recycling Ratio'
        #         },
        #         'data': np.array(
        #             0.02,
        #             dtype=ds_data_vars_f4
        #         )
        # },
        # # 1D
        # 'rice-rainfed': {
        #         'dims': (                               # variable dimensions, 1D
        #                 'time'
        #         ),
        #         'attrs': {
        #                 'standard_name':    'Crop Calendar',
        #                 'long_name':        'Crop Calendar'
        #         },
        #         'data': np.array(                           # variable data, np.array(, dtype=)
        #                 [
        #                     1, 2
        #                 ],
        #                 dtype=ds_data_vars_f4
        #         )
        # },

        # 2D, Integer
        'lu': {                                             # variable short name
                'dims': (                                   # variable dimensions
                        'y',
                        'x'
                ),
                'attrs': {                                  # variable attributes
                                                            # 'grid_mapping' linked with variable 'crs'
                        'grid_mapping':  'crs',
                        'standard_name': 'Landuse',
                        'long_name':     'Landuse',
                        'temp_res':      '',
                        'units':         '',
                        'from':          'FAO'
                },
                'data': np.array(                           # variable data, np.array(, dtype=)
                        [
                            [1, 2],
                            [3, 4],
                            [5, 6]
                        ],
                        dtype=ds_data_vars_i4
                )
        },
        # 2D, Float
        'dem': {                                            # variable short name
                'dims': (                                   # variable dimensions
                        'y',
                        'x'
                ),
                'attrs': {                                  # variable attributes
                                                            # 'grid_mapping' linked with variable 'crs'
                        'grid_mapping':  'crs',
                        'standard_name': 'Digital Elevation Model',
                        'long_name':     'DEM',
                        'temp_res':      '',
                        'units':         '',
                        'from':          'HydroSHED'
                },
                'data': np.array(                           # variable data, np.array(, dtype=)
                        [
                            [1, 2],
                            [3, 4],
                            [5, 6]
                        ],
                        dtype=ds_data_vars_f4
                )
        },
        'dir': {
                'dims': (
                        'y',
                        'x'
                ),
                'attrs': {
                        'grid_mapping':  'crs',
                        'standard_name': 'Digital Direction Model',
                        'long_name':     'DIR',
                        'temp_res':      '',
                        'units':         '',
                        'from':          'HydroSHED'
                },
                'data': np.array(
                        [
                            [1, 2],
                            [3, 4],
                            [5, 6]
                        ],
                        dtype=ds_data_vars_f4
                )
        },

        # 3D
        'pcp': {                                            # variable short name
                'dims': (                                   # variable dimensions
                        'time',
                        'y',
                        'x'
                ),
                'attrs': {                                  # variable attributes
                                                            # 'grid_mapping' linked with variable 'crs'
                        'grid_mapping':  'crs',
                        'standard_name': 'Precipitation',
                        'long_name':     'Precipitation',
                        'temp_res':      'day',
                        'units':         'mm',
                        'from':          'WaterPix'
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
                        dtype=ds_data_vars_f4
                )
        },
        'pet': {
                'dims': ('time', 'y', 'x'),
                'attrs': {
                        'grid_mapping':  'crs',
                        'standard_name': 'Potential EvapoTranspiration',
                        'long_name':     'Potential EvapoTranspiration',
                        'temp_res':      'day',
                        'units':         'mm',
                        'from':          'WaterPix'
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
                        dtype=ds_data_vars_f4
                )
        },
        'ret': {
                'dims': ('time', 'y', 'x'),
                'attrs': {
                        'grid_mapping':  'crs',
                        'standard_name': 'Reference EvapoTranspiration',
                        'long_name':     'Reference EvapoTranspiration',
                        'temp_res':      'day',
                        'units':         'mm',
                        'from':          'WaterPix'
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
                        dtype=ds_data_vars_f4
                )
        },
        'bet': {
                'dims': ('time', 'y', 'x'),
                'attrs': {
                        'grid_mapping':  'crs',
                        'standard_name': 'Blue EvapoTranspiration',
                        'long_name':     'Blue EvapoTranspiration',
                        'temp_res':      'day',
                        'units':         'mm',
                        'from':          'WaterPix'
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
                        dtype=ds_data_vars_f4
                )
        },
        'get': {
                'dims': ('time', 'y', 'x'),
                'attrs': {
                        'grid_mapping':  'crs',
                        'standard_name': 'Green EvapoTranspiration',
                        'long_name':     'Green EvapoTranspiration',
                        'temp_res':      'day',
                        'units':         'mm',
                        'from':          'WaterPix'
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
                        dtype=ds_data_vars_f4
                )
        },
        'et': {
                'dims': ('time', 'y', 'x'),
                'attrs': {
                        'grid_mapping':  'crs',
                        'standard_name': 'EvapoTranspiration',
                        'long_name':     'EvapoTranspiration',
                        'temp_res':      'day',
                        'units':         'mm',
                        'from':          'WaterPix'
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
                        dtype=ds_data_vars_f4
                )
        },
        'n': {
                'dims': ('time', 'y', 'x'),
                'attrs': {
                        'grid_mapping':  'crs',
                        'standard_name': 'Rainy Days',
                        'long_name':     'Rainy Days',
                        'temp_res':      'day',
                        'units':         '',
                        'from':          'WaterPix'
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
                        dtype=ds_data_vars_f4
                )
        },
        'ndm': {
                'dims': ('time', 'y', 'x'),
                'attrs': {
                        'grid_mapping':  'crs',
                        'standard_name': 'National Drought Model',
                        'long_name':     'National Drought Model',
                        'temp_res':      'day',
                        'units':         '',
                        'from':          'WaterPix'
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
                        dtype=ds_data_vars_f4
                )
        },
        'lai': {
                'dims': ('time', 'y', 'x'),
                'attrs': {
                        'grid_mapping':  'crs',
                        'standard_name': 'Leaf Area Index',
                        'long_name':     'Leaf Area Index',
                        'temp_res':      'day',
                        'units':         '',
                        'from':          'WaterPix'
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
                        dtype=ds_data_vars_f4
                )
        },
        'bf': {
                'dims': ('time', 'y', 'x'),
                'attrs': {
                        'grid_mapping':  'crs',
                        'standard_name': 'Baseflow',
                        'long_name':     'Baseflow',
                        'temp_res':      'day',
                        'units':         '',
                        'from':          'WaterPix'
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
                        dtype=ds_data_vars_f4
                )
        },
        'sr': {
                'dims': ('time', 'y', 'x'),
                'attrs': {
                        'grid_mapping':  'crs',
                        'standard_name': 'Surface Runoff',
                        'long_name':     'Surface Runoff',
                        'temp_res':      'day',
                        'units':         '',
                        'from':          'WaterPix'
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
                        dtype=ds_data_vars_f4
                )
        },
        'dro': {
                'dims': ('time', 'y', 'x'),
                'attrs': {
                        'grid_mapping':  'crs',
                        'standard_name': 'Incremental Runoff',
                        'long_name':     'Incremental Runoff',
                        'temp_res':      'day',
                        'units':         '',
                        'from':          'WaterPix'
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
                        dtype=ds_data_vars_f4
                )
        },
        'tr': {
                'dims': ('time', 'y', 'x'),
                'attrs': {
                        'grid_mapping':  'crs',
                        'standard_name': 'Total Runoff',
                        'long_name':     'Total Runoff',
                        'temp_res':      'day',
                        'units':         '',
                        'from':          'WaterPix'
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
                        dtype=ds_data_vars_f4
                )
        },
        'perc': {
                'dims': ('time', 'y', 'x'),
                'attrs': {
                        'grid_mapping':  'crs',
                        'standard_name': 'Percolation',
                        'long_name':     'Percolation',
                        'temp_res':      'day',
                        'units':         '',
                        'from':          'WaterPix'
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
                        dtype=ds_data_vars_f4
                )
        },
        'dperc': {
                'dims': ('time', 'y', 'x'),
                'attrs': {
                        'grid_mapping':  'crs',
                        'standard_name': 'Incremental Percolation',
                        'long_name':     'Incremental Percolation',
                        'temp_res':      'day',
                        'units':         '',
                        'from':          'WaterPix'
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
                        dtype=ds_data_vars_f4
                )
        },
        'supply': {
                'dims': ('time', 'y', 'x'),
                'attrs': {
                        'grid_mapping':  'crs',
                        'standard_name': 'Supply',
                        'long_name':     'Supply',
                        'temp_res':      'day',
                        'units':         '',
                        'from':          'WaterPix'
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
                        dtype=ds_data_vars_f4
                )
        }
    }
})

# xarray Dataset, write to NetCDF file
ds.to_netcdf(
    file,
    mode='w',
    format='NETCDF4',                                       # watools uses 'NETCDF4_CLASSIC'
    engine='netcdf4',
    encoding={
        # coord
        'lon': {
            'dtype':        ds_coords_dtype
        },
        'lat': {
            'dtype':        ds_coords_dtype
        },
        # CRS
        'crs': {
            'dtype':        ds_data_vars_i4
        },
        # 2D, Integer
        'lu': {
            'dtype':        ds_data_vars_i4,
            '_FillValue':   ds_FillValue_i4,
            'scale_factor': ds_data_vars_f4(1.0),
            'add_offset':   ds_data_vars_f4(0.0)
        },
        # 2D, Float
        'pcp': {
            'dtype':        ds_data_vars_f4,
            '_FillValue':   ds_FillValue_f4,
            'scale_factor': ds_data_vars_f4(1.0),
            'add_offset':   ds_data_vars_f4(0.0)
        },
        'pet': {
            'dtype':        ds_data_vars_f4,
            '_FillValue':   ds_FillValue_f4,
            'scale_factor': ds_data_vars_f4(1.0),
            'add_offset':   ds_data_vars_f4(0.0)
        }
    }
)

# xarray Dataset, close NetCDF file
ds.close()

# xarray Dataset, open from NetCDF file
with xr.open_dataset(file) as ds:
    print(ds)
    # print(ds.keys())
