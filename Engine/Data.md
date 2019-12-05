# IHEWAstandard.Engine.Data

Define the **Engine.Data standard** of WaterAccounting Tools.

**TOC**

  - [Standard](#standard)
    - [File name](#file-name)
    - [Attributes/Metadata](#attributesmetadata)
    - [Dimensions](#dimensions)
    - [Coordinates variables](#coordinates-variables)
    - [Data variables](#data-variables)
      - [CRS](#coordinate-reference-system-do-not-change-crs)
      - [Hydrological](#hydrological-variables)
  - [Resources](#resources)
  - [Examples](#examples)


## Standard

### File name

| Template                 | Example                                                            | Remarks |
| -----------------------: | ------------------------------------------------------------------ | ------- |
| Engine2.Input.Day.nc     | `EngineNumber`.`Input/Output`.`TemporalResolution`.`FileExtension` |         |

> The following template use '**day**' as temporal resolution.

### Attributes/Metadata

| Name           | Type   | Example           | Description                                                |
| -------------: | ------ | ----------------- | ---------------------------------------------------------- |
|  **Basic Info**                                                                                          |
| version        | String | 'v0'              | The version of this template NetCDF is 'v0', major release |
| standard       | String | 'WaterAccounting' | This version applies standard of 'WaterAccounting'         |
|  **Engine Info**                                                                                         |
| engine_num     | String | '2'               | The data is created for engine number '2'                  |
| engine_use     | String | 'Input'           | This engine use the data as 'input'                        |
| model_name     | String | 'Hyperloop'       | This engine name is 'Hyperloop'                            |
| model_version  | String | 'v0.0.1'          | This engine version is 'v0.0.1'                            |
|  **Creater Info**                                                                                        |
| created_by     | String | 'IHE'             | This data is created by owner 'IHE'                        |
| created_time   | String | '2019-12-03'      | This data is created at 'yyyy-mm-dd'                       |
| created_model  | String | 'WaterPix'        | This data is created by model 'WaterPix'                   |
|  **GTiff Format**                                                                                        |
| CRS            | String | 'EPSG:4326 - WGS 84 - Geographic' | CRS name linked with variable 'crs'        |
| originX        | Double | 0.0               | West                                                       |
| originY        | Double | 20.0              | North                                                      |
| rasterW        | Double | 10.0              | Raster Width,  image pixel size 10.0                       |
| rasterH        | Double | -10.0             | Raster Height, image pixel size 10.0                       |

### Dimensions

time, y, x => time, lat, lon

Template:

```Python
'dims': ('time', 'y', 'x')
```

### Coordinates variables

Template:

```Python
'lon': {                                        # longitude,    np.ndarray
        'dims': ('y', 'x'),
        'attrs': {
                'standard_name': 'Longitude',
                'long_name':     'Longitude',
                'units':         'degree',
                'axis':          'x'
        },
        'data': np.array(
                [
                    [0, 10],
                    [0, 10],
                    [0, 10]
                ],
                dtype=np.float32
        )
},
'lat': {                                        # latitude,    np.ndarray
        'dims': ('y', 'x'),
        'attrs': {
                'standard_name': 'Latitude',
                'long_name':     'Latitude',
                'units':         'degree',
                'axis':          'y'
        },
        'data': np.array(
                [
                    [20, 20],
                    [10, 10],
                    [0,  0]
                ],
                dtype=np.float32
        )
},
'time': {                                       # time,        np.ndarray
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
```

### Data variables

#### Coordinate Reference System, **DO NOT CHANGE 'crs'!**

Template:

```Python
'crs': {                                        # variable short name, 'crs': 'EPSG:4326 - WGS 84 - Geographic'
        'dims': (),
        'attrs': {
                'standard_name':                'CRS',
                'long_name':                    'Coordinate Reference System',
                'grid_mapping_name':            'latitude_longitude',
                
                'spatial_ref':                  'GEOGCS['
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
                'longitude_of_prime_meridian':  0.0,
                'semi_major_axis':              6378137.0,
                'inverse_flattening':           298.257223563
        },
        'data': np.NaN
}
```

#### Hydrological Variables

Some templates and standards can be found in 
[IHEWAstandard/resources/Products.xlsx](https://github.com/wateraccounting/IHEWAstandard/tree/master/resources).

[Archived Engine.Data.Engine1](./Archived-Data.md#engine-1)
[Archived Engine.Data.Engine2](./Archived-Data.md#engine-2)

| Variable Name/Code | Standard Name | units | Description |
| -----------------: | ------------- | ----- | ----------- |
| 2D  |  |  |  |  |
| `dem`              | Digital Elevation Model |  |  |
| `dir`              | Direction     |  |  |
| 3D  |  |  |  |  |
| `pcp`              | Precipitation | mm    | The value of each pixel represents the total of daily precipitation in the year expressed in mm |
| `pet`              | Potential EvapoTranspiration | mm    | The value of each pixel represents the total of daily Potential EvapoTranspiration in the year expressed in mm |
| `ret`              | Reference EvapoTranspiration |  |  |
| `bet`              | Blue EvapoTranspiration |  |  |
| `get`              | Green EvapoTranspiration |  |  |
| `et`               | Evapotranspiration |  |  |
| `n`                | Rainy Days |  |  |
| `ndm`              | National Drought Model |  |  |
| `lai`              | Leaf Area Index |  |  |
| `bf`               | Baseflow |  |  |
| `sr`               | Surface Runoff |  |  |
| `dro`              | Incremental Runoff|  |  |
| `tr`               | Total  Runoff |  |  |
| `perc`             | Percolation|  |  |
| `dperc`            | Incremental Percolation|  |  |
| `supply`           | Supply|  |  |

Template 2D variable:

```Python
'dem': {
        'dims': (                               # variable dimensions, 2D
                'y',
                'x'
        ),
        'attrs': {                              # variable attributes
                                                # 'grid_mapping' linked with variable 'crs'
                'grid_mapping':  'crs',
                'standard_name': 'Digital Elevation Model',
                'long_name':     'DEM',
                'units':         '',
                'from':          'HydroSHED'
        },
        'data': np.array(                       # variable data, np.array(, dtype=)
                [
                    [1, 2],
                    [3, 4],
                    [5, 6]
                ],
                dtype=ds_data_vars_dtype
        )
```

Template 3D variable:

```Python
'pcp': {                                        # variable short name
        'dims': (                               # variable dimensions
                'time',
                'y',
                'x'
        ),
        'attrs': {                              # variable attributes
                'grid_mapping':  'crs',         # 'grid_mapping' linked with variable 'crs'
                'standard_name': 'Precipitation',
                'long_name':     'Precipitation',
                'temp_res':      'day',
                'units':         'mm',
                'from':          'WaterPix'
        },
        'data': np.array(                       # variable data, np.array(, dtype=)
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
        )
},
```

## Resources


# [Examples](examples/README.md#data)
