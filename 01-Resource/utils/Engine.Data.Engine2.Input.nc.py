import os

import datetime
import numpy as np
import pandas as pd
import xarray as xr

# print(os.getcwd())
# print(os.path.dirname(os.path.abspath(__file__)))
fpath = os.path.dirname(os.path.abspath(__file__))

# %% Engine2.Input.nc
file = os.path.join(fpath, '../', '../', 'Engine', 'examples', 'Engine2.Input.nc')
if os.path.exists(file):
    os.remove(file)

# xarray Dataset, define
ds_FillValue_i4 = -9999
ds_FillValue_f4 = np.NaN
ds_FillValue_f8 = np.NaN

ds_coords_dtype = np.float32

ds_data_vars_i4 = np.int32
ds_data_vars_f4 = np.float32
ds_data_vars_f8 = np.float64

ds = xr.Dataset.from_dict(
{
    'attrs': {
        # Meta
        'version':          'v0',                           # The version of this template NetCDF is 'v0', major release number of Github & Pypi
        'standard':         'WaterAccounting',              # This version applies standard of 'WaterAccounting'

        # For engine
        'engine_num':       '2',                            # The data is created for engine '2'
        'engine_use':       'Input',                        # The data is used as 'input' for engine2
        'model_name':       'Hyperloop',                    # The engine model,   linked with release name
        'model_version':    'v0.0.1',                       # The engine version, linked with release version

        # Created by
        'created_by':       'IHE',                          # This data is created by owner 'IHE'
        # 'created_time':     '2019-12-31 00:00:00',        # This data is cre0ated at time  'yyyy-mm-dd HH:MM:SS'
        # 'created_time':     '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime(2019, 12, 31, 0, 0, 0)),
        'created_time':     '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()),
        'created_model':    'WaterPix',                     # This data is created by model 'WaterPix'

        # GTiff format
                                                            # GTiff Origin, [West, North]
                                                            # GTiff Extent, [West, South] to [East, North]
                                                            # GTiff         rasterWidth  = 10
                                                            # GTiff         rasterHeight = -10
                                                            # Image         pixelWidth   = 10
                                                            # Image         pixelHeight  = 10
                                                            # CRS name,     linked with variable 'crs'

        # GIS
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
                        'standard_name': 'longitude',
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
                        dtype=ds_data_vars_f4
                )
        },
        'lat': {                                            # latitude,    np.ndarray
                'dims': ('y', 'x'),
                'attrs': {
                        'standard_name': 'latitude',
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
                        dtype=ds_data_vars_f4
                )
        },
        'time': {                                           # time,        np.ndarray
                'dims': ('time'),
                'attrs': {
                        'standard_name': 'time',
                        'long_name':     'Time'
                },
                'data': np.array(                           # Temporal resolution, linked to file name
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
        # 'VITO':
        #     _CoordinateTransformType = "Projection"
        #     _CoordinateAxisTypes = "GeoX GeoY"
        #     spatial_ref =
        #     'GEOGCS['
        #         'WGS 84,'
        #         'DATUM['
        #             'WGS_1984,'
        #             'SPHEROID['
        #                 'WGS 84,'
        #                 '6378137,'
        #                 '298.257223563,'
        #                 'AUTHORITY['
        #                     'EPSG,'
        #                     '7030'
        #                 ']'
        #             '],'
        #             'AUTHORITY['
        #                 'EPSG,'
        #                 '6326'
        #             ']'
        #         '],'
        #         'PRIMEM['
        #             'Greenwich,'
        #             '0,'
        #             'AUTHORITY['
        #                 'EPSG,'
        #                 '8901'
        #             ']'
        #         '],'
        #         'UNIT['
        #             'degree,'
        #             '0.01745329251994328,'
        #             'AUTHORITY['
        #                 'EPSG,'
        #                 '9122'
        #             ']'
        #         '],'
        #         'AUTHORITY['
        #             'EPSG,'
        #             '4326'
        #         ']'
        #     ']'
        'crs': {                                            # variable short name, 'crs': 'EPSG:4326 - WGS 84 - Geographic'
                                                            # DO NOT CHANGE 'crs'!
                'dims': (),
                'attrs': {
                        'standard_name':                    'coordinate_reference_system',
                        'long_name':                        'Lon/Lat Coords in WGS84',
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
        'RecyclingRatio': {
                'dims': (),
                'attrs': {
                        'standard_name': 'recycling_ratio',
                        'long_name':     'Recycling Ratio',
                        'units':         '',
                        'from':          'Parameter'
                },
                'data': np.array(
                        0.02,
                        dtype=ds_data_vars_f8
                )
        },

        # 1D
        'Q': {
                'dims': (                                   # variable dimensions, 1D
                        'time'
                ),
                'attrs': {                                  # variable attributes
                        'standard_name': 'discharge',
                        'long_name':     'Discharge',
                        'units':         'm3.d',
                        'from':          'Measurement'
                },
                'data': np.array(                           # variable data, np.array(, dtype=)
                        [
                            1, 2
                        ],
                        dtype=ds_data_vars_f8
                )
        },

        # 2D, Integer
        'LU': {                                             # variable short name
                'dims': (                                   # variable dimensions
                        'y',
                        'x'
                ),
                'attrs': {                                  # variable attributes
                                                            # 'grid_mapping' linked with variable 'crs'
                        'grid_mapping':  'crs',
                        'standard_name': 'landuse_landcover',
                        'long_name':     'Landuse Landcover',
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
        'DEM': {                                            # variable short name
                'dims': (                                   # variable dimensions
                        'y',
                        'x'
                ),
                'attrs': {                                  # variable attributes
                                                            # 'grid_mapping' linked with variable 'crs'
                        'grid_mapping':  'crs',
                        'standard_name': 'digital_elevation_model',
                        'long_name':     'Digital Elevation Model',
                        'units':         'm',
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
        'DIR': {
                'dims': (
                        'y',
                        'x'
                ),
                'attrs': {
                        'grid_mapping':  'crs',
                        'standard_name': 'drainage_direction_model',
                        'long_name':     'Drainage Direction Model',
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
        'PCP': {                                            # variable short name
                'dims': (                                   # variable dimensions
                        'time',
                        'y',
                        'x'
                ),
                'attrs': {                                  # variable attributes
                                                            # 'grid_mapping' linked with variable 'crs'
                        'grid_mapping':  'crs',
                        'standard_name': 'precipitation',
                        'long_name':     'Precipitation',
                        'units':         'mm.d',
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
                                [2, 3],
                                [4, 5],
                                [6, 1]
                            ]
                        ],
                        dtype=ds_data_vars_f4
                )
        },
        'ETP': {
                'dims': (
                        'time',
                        'y',
                        'x'
                ),
                'attrs': {
                        'grid_mapping':  'crs',
                        'standard_name': 'potential_evapoTranspiration',
                        'long_name':     'Potential EvapoTranspiration',
                        'units':         'mm.d',
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
                                [2, 3],
                                [4, 5],
                                [6, 1]
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
        # coords
        'lon': {
            'dtype':        ds_data_vars_f4
        },
        'lat': {
            'dtype':        ds_data_vars_f4
        },

        # data_vars
        # CRS
        'crs': {
            'dtype':        ds_data_vars_f4,
            '_FillValue':   ds_FillValue_f4,
        },
        # 1D,
        'Q': {
            'dtype':        ds_data_vars_f4,
            '_FillValue':   ds_FillValue_f4,
            'scale_factor': ds_data_vars_f4(1.0),
            'add_offset':   ds_data_vars_f4(0.0)
        },
        # 2D, Integer
        'LU': {
            'dtype':        ds_data_vars_i4,
            '_FillValue':   ds_FillValue_i4,
            'scale_factor': ds_data_vars_f4(1.0),
            'add_offset':   ds_data_vars_f4(0.0)
        },
        # 2D, Float
        'PCP': {
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
