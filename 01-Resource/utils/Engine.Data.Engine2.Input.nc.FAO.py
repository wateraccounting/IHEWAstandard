import os
# print(os.getcwd())

import datetime
import numpy as np
import pandas as pd
import xarray as xr

# ##### #
# Input #
# ##### #
input_path_data = r'./'
input_fname = r'p_monthly.nc'
input_var = 'Precipitation'
input_dim_time = 'time'
input_dim_lat = 'latitude'
input_dim_lon = 'longitude'

# variable, dimension
# (time=120, latitude=4547, longitude=5444)

# ###### #
# Output #
# ###### #
output_var = 'p'
output_var_long_name = 'Precipitation'
output_var_standard_name = 'precipitation'
output_var_units = 'mm/month'
output_var_complevel = 9  # valide level: 1 to ; no compress: 0

output_var_dim_time = 12
# years = np.arange(start=2009, stop=(2018 + 1), step=1, dtype=np.int)
years = np.arange(start=2009, stop=(2009 + 1), step=1, dtype=np.int)

# file name
output_path_data = r'./Basin_name/Input/netCDF/{var}'.format(var=output_var)
output_fname_template = '{year}.nc'
# output_fname_template = '{year}-{var}.nc'

# ##### #
# Start #
# ##### #
file_i = os.path.join(input_path_data, input_fname)
if not os.path.exists(file_i):
    print('"{}" not found!'.format(file_i))
else:
    # define, xarray Dataset
    ds_data_vars_f4 = np.float32
    ds_FillValue_f4 = ds_data_vars_f4(-9999.0)

    ds_data_vars_f8 = np.float64
    ds_FillValue_f8 = ds_data_vars_f8(-9999.0)

    # Load data
    with xr.open_dataset(file_i) as ds_i:
        # print(ds_i)

        # Attributes: attrs, dims, coords, data_vars
        output_var_dim_lat = ds_i.dims[input_dim_lat]
        output_var_dim_lon = ds_i.dims[input_dim_lon]

        t = ds_i.coords[input_dim_time].values
        y = ds_i.coords[input_dim_lat].values
        x = ds_i.coords[input_dim_lon].values
        print('t', t[0], t[-1])
        print('y', y[0], y[-1])
        print('x', x[0], x[-1])
        lon, lat = np.meshgrid(x, y, sparse=False)
        print('lon', lon[0, 0], lon[0, -1])
        print('lat', lat[0, 0], lat[-1, 0])

    # Write data
    for iyear in range(len(years)):
        year = years[iyear]
        istart = iyear * output_var_dim_time
        iend = (iyear + 1) * output_var_dim_time

        output_time = np.array([pd.Timestamp(dtime) for dtime in t[istart:iend]])
        output_data = ds_i.data_vars[input_var][istart:iend].values

        # Check output folder
        if not os.path.exists(output_path_data):
            os.makedirs(output_path_data)

        file_o = os.path.join(output_path_data,
                              output_fname_template.format(year=year, var=output_var))
        if os.path.exists(file_o):
            os.remove(file_o)

        print(file_o)

        # xarray Dataset, create data
        ds_o_dict = {
            'attrs': {
                # !!!!!!!!! #
                # GIS, keep #
                # !!!!!!!!! #
                'CRS': 'EPSG:4326 - WGS 84 - Geographic',

                # !!!! #
                # Meta #
                # !!!! #
                # Fao
                'title': '',
                'id': '',
                'processing_level': '',
                'comment': '',
                'date_created': '',
                'creator_name': '',
                'creator_email': '',
                'institution': '',
                'project': '',
                'geospatial_bounds': '',
                'geospatial_bounds_crs': '',
                'geospatial_lat_min': '',
                'geospatial_lat_max': '',
                'geospatial_lon_min': '',
                'geospatial_lon_max': '',
                'time_coverage_start': '',
                'time_coverage_end': '',
                'time_coverage_resolution': '',
                'geospatial_lat_units': '',
                'geospatial_lat_resolution': '',
                'geospatial_lon_units': '',
                'geospatial_lon_resolution': '',
                'date_modified': '',
                'date_metadata_modified': '',
                'data_type': '',
                'metadata_link': '',
                'references': '',
                'description': '',

                # # From QPan, can comment
                # 'version': 'v0',
                # 'standard': 'WaterAccounting',
                # 'engine_num': '2',
                # 'engine_use': 'Input',
                # 'model_name': 'Hyperloop',
                # 'model_version': 'v0.0.1',
                # 'created_by': 'IHE',
                # 'created_time': '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()),
                # 'created_model': 'WaterPix',
            },
            'dims': {
                'time': output_var_dim_time,
                'y': output_var_dim_lat,
                'x': output_var_dim_lon
            },
            'coords': {
                'lat': {
                    'dims': ('y', 'x'),
                    'attrs': {
                        'standard_name': 'latitude',
                        'long_name': 'Latitude',
                        'units': 'degrees_north',
                        'axis': 'y'
                    },
                    'data': lat.astype(ds_data_vars_f4)
                    # np.array(
                    #     [
                    #         [20, 20],
                    #         [10, 10],
                    #         [0, 0]
                    #     ],
                    #     dtype=ds_data_vars_f4
                    # )
                },
                'lon': {
                    'dims': ('y', 'x'),
                    'attrs': {
                        'standard_name': 'longitude',
                        'long_name': 'Longitude',
                        'units': 'degrees_east',
                        'axis': 'x'
                    },
                    'data': lon.astype(ds_data_vars_f4)
                    # np.array(
                    #     [
                    #         [0, 10],
                    #         [0, 10],
                    #         [0, 10]
                    #     ],
                    #     dtype=ds_data_vars_f4
                    # )
                },
                'time': {
                    'dims': ('time'),
                    'attrs': {
                        'standard_name': 'time',
                        'long_name': 'Time'
                    },
                    'data': output_time
                }
            },
            'data_vars': {
                # !!!!!!!!!!!!!!!!!!! #
                # DO NOT CHANGE 'crs' #
                # !!!!!!!!!!!!!!!!!!! #
                'crs': {
                    'dims': (),
                    'attrs': {
                        'standard_name': 'coordinate_reference_system',
                        'long_name': 'Lon/Lat Coords in WGS84',
                        'grid_mapping_name': 'latitude_longitude',

                        'spatial_ref': 'GEOGCS['
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
                        'longitude_of_prime_meridian': 0.0,
                        'semi_major_axis': 6378137.0,
                        'inverse_flattening': 298.257223563
                    },
                    'data': ds_FillValue_f4
                },

                # 3D
                output_var: {
                    'dims': (
                        'time',
                        'y',
                        'x'
                    ),
                    'attrs': {
                        # 'grid_mapping' linked with variable 'crs'
                        'grid_mapping': 'crs',
                        'standard_name': output_var_standard_name,
                        'long_name': output_var_long_name,
                        'units': output_var_units
                    },
                    'data': output_data.astype(ds_data_vars_f4)
                }
            }
        }

        # Compression,
        # {'chunksizes', 'fletcher32', 'contiguous', 'complevel', 'shuffle', 'least_significant_digit', '_FillValue', 'zlib', 'dtype'}
        # http://unidata.github.io/netcdf4-python/netCDF4/index.html#section9
        if 0 < output_var_complevel < 10:
            ds_o_encoding = {
                # coords
                'lat': {
                    'zlib': True,
                    'complevel': output_var_complevel,
                    'least_significant_digit': 3
                },
                'lon': {
                    'zlib': True,
                    'complevel': output_var_complevel,
                    'least_significant_digit': 3
                },
                # 3D
                output_var: {
                    'dtype': ds_data_vars_f4,
                    '_FillValue': ds_FillValue_f4,
                    'scale_factor': ds_data_vars_f4(1.0),
                    'add_offset': ds_data_vars_f4(0.0),
                    'zlib': True,
                    'complevel': output_var_complevel,
                    'least_significant_digit': 3
                }
            }
        else:
            ds_o_encoding = {
                # coords
                'lat': {
                    'zlib': False,
                    'least_significant_digit': 3
                },
                'lon': {
                    'zlib': False,
                    'least_significant_digit': 3
                },
                # 3D
                output_var: {
                    'dtype': ds_data_vars_f4,
                    '_FillValue': ds_FillValue_f4,
                    'scale_factor': ds_data_vars_f4(1.0),
                    'add_offset': ds_data_vars_f4(0.0),
                    'zlib': False,
                    'least_significant_digit': 3
                }
            }

        # xarray Dataset, write to file
        ds_o = xr.Dataset.from_dict(ds_o_dict)
        ds_o.to_netcdf(
            file_o,
            mode='w',
            format='NETCDF4',  # watools uses 'NETCDF4_CLASSIC'
            engine='netcdf4',
            encoding=ds_o_encoding
        )

        # xarray Dataset, close file
        ds_o.close()

        # # xarray Dataset, check created file
        # with xr.open_dataset(file_o) as ds:
        #     print(ds)
        #     # print(ds.keys())

    # close input NetCDF file
    ds_i.close()
