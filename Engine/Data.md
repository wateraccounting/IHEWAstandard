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
  - [Engine 1](#engine-1)
    - [Input, NetCDF](#engine-1-input-netcdf)
    - [Output, NetCDF](#engine-1-output-netcdf)
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

[Archived Engine.Data.Engine2](./Archived-Data.md#engine-2)

| Variable Name/Code | Standard Name | units | Description |
| -----------------: | ------------- | ----- | ----------- |
| 2D  |  |  |  |  |
| `dem`              | Digital Elevation Model |  |  |
| `dir`              | Direction     |  |  |
| 3D  |  |  |  |  |
| `pcp`              | Precipitation | mm    | The value of each pixel represents the total of daily precipitation in the year expressed in mm |
| `pet`              | Potential EvapoTranspiration | mm    | The value of each pixel represents the total of daily Potential EvapoTranspiration in the year expressed in mm |
| `et`               | Evapotranspiration |  |  |
| `ret`              | Reference EvapoTranspiration |  |  |
| `bet`              | Blue EvapoTranspiration |  |  |
| `get`              | Green EvapoTranspiration |  |  |
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


## Engine 1

Example from WaterPix.

### Engine 1, Input, NetCDF

#### Dimensions

#### Coordinates

#### Data variables

  - `inp_crs` = ncv['**crs**']
  - `inp_lat` = ncv['**latitude**']
  - `inp_lon` = ncv['**longitude**']
  - `inp_time` = ncv['**time_yyyymm**']
  - `inp_basinb` = ncv['**BasinBuffer**']
  - `p_fv` = ncv['**Precipitation_M**']._FillValue
  - `et_fv` = ncv['**Evapotranspiration_M**']._FillValue
  - `eto_fv` = ncv['**ReferenceET_M**']._FillValue
  - `lai_fv` = ncv['**LeafAreaIndex_M**']._FillValue
  - `swi_fv` = ncv['**SWI_M**']._FillValue
  - `swio_fv` = ncv['**SWIo_M**']._FillValue
  - `swix_fv` = ncv['**SWIx_M**']._FillValue
  - `qratio_fv` = ncv['**RunoffRatio_Y**']._FillValue
  - `rainydays_fv` = ncv['**RainyDays_M**']._FillValue
  - `thetasat_fv` = ncv['**SaturatedWaterContent**']._FillValue
  - `rootdepth_fv` = ncv['**RootDepth**']._FillValue


### Engine 1, Output, NetCDF

#### Dimensions

  - Monthly, **('time_yyyymm', 'latitude', 'longitude')**
  - Yearly, **('time_yyyy', 'latitude', 'longitude')**

```Python
lat_dim  = out_nc.createDimension(inp_lat.standard_name, lat_n)
lon_dim  = out_nc.createDimension(inp_lon.standard_name, lon_n)
time_dim = out_nc.createDimension('time_yyyymm',         time_n)
year_dim = out_nc.createDimension('time_yyyy',           years_n)
```

#### Coordinates

  - _Reference system_, `crs_var`, **inp_crs.standard_name**, '`i`'
    - crs_var.standard_name
    - crs_var.grid_mapping_name
    - crs_var.crs_wkt
  - _Latitude_, `lat_var`, **latitude**, 'f8'
    - lat_var.units
    - lat_var.standard_name
  - _Longitude_, `lon_var`, **longitude**, 'f8'
    - lon_var.units
    - lon_var.standard_name
  - _Time (month)_, `time_var`, '**time_yyyymm**', '`l`'
    - time_var.standard_name
    - time_var.format
  - _Time (year)_, `year_var`, '**time_yyyy**', '`l`'
    - year_var.standard_name = 'time_yyyy'
    - year_var.format = 'yyyy'

#### Data variables 

  - _Surface runoff_
    - monthly, **SurfaceRunoff_M**, `ss_var`, _`mm/month`_
    - yearly, **SurfaceRunoff_Y**, `ssy_var`, _`mm/year`_
    - dtype, 'f8'
  - _Baseflow_
    - monthly, **Baseflow_M**, `bf_var`, _`mm/month`_
    - yearly, **Baseflow_Y**, `bfy_var`, _`mm/year`_
    - dtype, 'f8'
  - _Total runoff_
    - monthly, **TotalRunoff_M**, `sr_var`, _`mm/month`_
    - yearly, **TotalRunoff_Y**, `sry_var`, _`mm/year`_
    - dtype, 'f8'
  - _Storage change - soil moisture_
    - monthly, **StorageChange_M**, `dsm_var`, _`mm/month`_
    - yearly, **StorageChange_Y**, `dsmy_var`, _`mm/year`_
    - dtype, 'f8'
  - _Percolation_
    - monthly, **Percolation_M**, `per_var`, _`mm/month`_
    - yearly, **Percolation_Y**, `pery_var`, _`mm/year`_
    - dtype, 'f8'
  - _Supply_
    - monthly, **Supply_M**, `sup_var`, _`mm/month`_
    - yearly, **Supply_Y**, `supy_var`, _`mm/year`_
    - dtype, 'f8'
  - _Green Evapotranspiration_
    - monthly, **ETgreen_M**, `etgm_var`, _`mm/month`_
    - yearly, **ETgreen_Y**, `etg_var`, _`mm/year`_
    - dtype, 'f8'
  - _Blue Evapotranspiration_
    - monthly, **ETblue_M**, `etbm_var`, _`mm/month`_
    - yearly, **ETblue_Y**, `etb_var`, _`mm/year`_
    - dtype, 'f8'
  - _Rainfed pixels_
    - yearly, **RainfedPixels_Y**, `gpix_var`, _`-`_
    - dtype, 'f8'
  - _Round code_
    - yearly, **RoundCode**, `rco_var`, _`None`_
    - dtype, '`l`'
  - _Root depth soil moisture_
    - monthly, **RootDepthSoilMoisture_M**, `rdsm_var`, _`cm3/cm3`_
    - dtype, 'f8'
  - _Calibration parameter - infiltration depth_
    - yearly, **InfiltrationDepth_Y**, `infz_var`, _`mm`_
    - dtype, 'f8'
  - _Incremental surface runoff_
    - monthly, **IncrementalRunoff_M**, `incss_var`, _`mm/month`_
    - yearly, **IncrementalRunoff_Y**, `incssy_var`, _`mm/year`_
    - dtype, 'f8'
  - _Incremental percolation_
    - yearly, **IncrementalPercolation_Y**, `incpery_var`, _`mm/year`_
    - dtype, 'f8'
  - _Water use efficiency_
    - monthly, **WaterUseEfficiency_M**, `effi_var`, _`-`_
    - yearly, **WaterUseEfficiency_Y**, `effiy_var`, _`-`_
    - dtype, 'f8'
  - _Percolation fit - parameter 'a'_
    - yearly, **a_Y**, `a_var`, _`None`_
    - dtype, 'f8'
  - _Percolation fit - parameter 'b'_
    - yearly, **b_Y**, `b_var`, _`None`_
    - dtype, 'f8'


# [Examples](examples/README.md#data)
