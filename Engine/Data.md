# IHEWAstandard.Engine.Data

Define the **Engine.Data standard** of WaterAccounting Tools.

**TOC**

  - [Standard](#standard)
    - [File name](#file-name)
    - [Attributes/Metadata](#attributesmetadata)
    - [Dimensions](#dimensions)
    - [Coordinates variables](#coordinates-variables)
    - [Data variables](#data-variables)
  - [Resources](#resources)
  - [Examples](#examples)


## Standard

[watools.General.data_convertions.Save_as_NC()](https://github.com/wateraccounting/watools/blob/master/General/data_conversions.py#L279)

### File name

| Template                 | Example                                                            | Remarks |
| -----------------------: | ------------------------------------------------------------------ | ------- |
| Engine2.Input.Day.nc     | `EngineNumber`.`Input/Output`.`TemporalResolution`.`FileExtension` |         |

> The following template use '**day**' as temporal resolution.

### Attributes/Metadata

> inculded in NetCDF file

| Name           | Type    | Example           | Description                                                |
| -------------: | ------- | ----------------- | ---------------------------------------------------------- |
|  **Basic Info**                                                                                           |
| version        | String  | 'v0'              | The version of this template NetCDF is 'v0', major release |
| standard       | String  | 'WaterAccounting' | This version applies standard of 'WaterAccounting'         |
|  **Engine Info**                                                                                          |
| engine_num     | String  | '2'               | The data is created for engine number '2'                  |
| engine_use     | String  | 'Input'           | This engine use the data as 'input'                        |
| model_name     | String  | 'Hyperloop'       | This engine model name is 'Hyperloop'                      |
| model_version  | String  | 'v0.0.1'          | This engine model version is 'v0.0.1'                      |
|  **Creater Info**                                                                                         |
| created_by     | String  | 'IHE'             | This data is created by owner 'IHE'                        |
| created_time   | String  | '2019-12-03'      | This data is created at 'yyyy-mm-dd'                       |
| created_model  | String  | 'WaterPix'        | This data is created by model 'WaterPix'                   |
|  **GTiff Format**                                                                                         |
| CRS            | String  | 'EPSG:4326 - WGS 84 - Geographic' | CRS name linked with variable 'crs'        |
| originX        | Double  |   0.0             | West                                                       |
| originY        | Double  |  20.0             | North                                                      |
| rasterW        | Double  |  10.0             | Raster Width,  image pixel size 10.0                       |
| rasterH        | Double  | -10.0             | Raster Height, image pixel size 10.0                       |

### Dimensions

> inculded in NetCDF file

time, y, x => time, lat, lon

_Template_

```Python
'dims': ('time', 'y', 'x')
```

### Coordinates variables

> inculded in NetCDF file

_Template_

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

**Coordinate Reference System**

> inculded in NetCDF file
> 
> **DO NOT CHANGE 'crs'!**

_Template_

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

**Variables**

Parameter, csv data

> not inculded in NetCDF file

| Variable Name/Code         | Standard Name                | units | Description                    |
| -------------------------: | ---------------------------- | ----- | ------------------------------ |
| **0D, Parameter**                                                                                  |
| `name`                     | Basin name                   |       | VGTB                           |
| `recycling_ratio`          | Ratio                        |       |                                |
| `water_year_start_month`   | Start month of water year    |       |                                |
| **0D, Extra**                                                                                      |
| `grace`                    | GRACE                        |       |                                |
| `grace_supply_split`       | GRACE                        |       |                                |
| `grace_split_alpha_bounds` | GRACE                        |       |                                |
| `ndm_max_original`         | National Drought Model       |       |                                |
| **1D, Parameter**                                                                                  |
| `dico_in`                  | subbasin in or outflow point |       |                                |
| `dico_out`                 | subbasin in or outflow point |       |                                |
| `fraction_xs`              | Fraction                     |       |                                |
| **1D, Calendar**                                                                                   |
| Crops                                                                                              |
| `rice-rainfed`             | Crops                        |       | Cereals                        |
| `rice-irrigated`           | Crops                        |       | Cereals                        |
| `tea`                      | Crops                        |       | Beverage crops                 |
| `fodder`                   | Crops                        |       | Other crops                    |
| `sugar cane`               | Crops                        |       | Non-cereals                    |
| Non-Crops                                                                                          |
| `meat`                     | Non-Crops                    |       | STATS_GSOV                     |
| `milk`                     | Non-Crops                    |       | STATS_GSOV                     |
| `timber`                   | Non-Crops                    |       | STATS_GSOV                     |
| `aquaculture`              | Non-Crops                    |       | STATS_GSOV                     |

GIS data

> inculded in NetCDF file

| Variables Name/Code                | Hyperloop                          | watools                            | WaPOR                              | Standard Name                    | units  | Description                         |
| ---------------------------------: | ---------------------------------- | ---------------------------------- | ---------------------------------- | -------------------------------- | ------ | ----------------------------------- |
| **2D, Static Map**                                                                                                                                                                                                                  |
| Integer                                                                                                                                                                                                                             |
| `lu`                               | `lu`                               | `Landuse`                          | `LCC`                              | VGTB                             |        |                     sh5             |
| `full_basin_mask`                  | `full_basin_mask`                  |                                    |                                    | VGTB                             |        |                                     |
| `masks`                            | `masks`                            |                                    |                                    | VGTB                             |        |                                     |
| `population_tif`                   | `population_tif`                   |                                    |                                    | VNM-POP                          |        | VNM_pph_v2b_2009                    |
| Float                                                                                                                                                                                                                               |
|                                    |                                    | `Water_Occurrence`                 |                                    | Water Occurrence                 |        |                     WPx             |
| `dem`                              | `dem`                              |                                    |                                    | Elevation                        |        |                     WPx             |
| `dir`                              | `dir`                              |                                    |                                    | Direction                        |        |                     WPx             |
| `equiped_sw_irrigation`            | `equiped_sw_irrigation`            |                                    |                                    | GMIA FAO                         |        | gmia_v5_aeisw_pct_aei_asc           |
| `wpl_tif`                          | `wpl_tif`                          |                                    |                                    | Grey Water Footprint             |        | WPL                                 |
| `environ_water_req`                | `environ_water_req`                |                                    |                                    | EF                               |        | EWR                                 |
|                                    |                                    | `Grey_Water_Footprint`             |                                    | Grey Water Footprint             |        |           sh4                       |
|                                    |                                    | `Theta_Saturated_Topsoil`          |                                    | Theta Saturated Topsoil          |        |           sh4                       |
|                                    |                                    | `Fraction_Surface_Water_Supply`    |                                    | Fraction Surface Water Supply    |        |                     sh5             |
| **3D, Timeserise Map**                                                                                                                                                                                                              |
| `pcp`                              | `pcp`                              | `Precipitation`                    | `PCP`                              | Precipitation                    | mm     | sh1  sh2  sh3  sh4  sh5             |
|                                    |                                    | `Evaporation`                      |                                    | Evaporation                      |        |      sh2                            |
|                                    |                                    | `Transpiration`                    |                                    | Transpiration                    |        |      sh2                            |
|                                    |                                    | `Interception`                     |                                    | Interception                     |        |      sh2                            |
| `pet`                              | `pet`                              |                                    |                                    | Potential EvapoTranspiration     | mm     |                                     |
| `ret`                              | `ret`                              | `Reference_Evapotranspiration`     | `RET`                              | Reference EvapoTranspiration     |        |           sh3  sh4  sh5             |
| `aet`                              |                                    | `Actual_Evapotranspiration`        | `RET`                              | Actual EvapoTranspiration        |        |      sh2  sh3  sh4  sh5             |
| `bet`                              | `bet`                              | `Blue_Evapotranspiration`          |                                    | Blue EvapoTranspiration          |        |           sh3  sh4                  |
| `get`                              | `get`                              | `Green_Evapotranspiration`         |                                    | Green EvapoTranspiration         |        |           sh3  sh4                  |
| `et`                               | `et`                               |                                    |                                    | Evapotranspiration               |        |                                     |
| `n`                                | `n`                                | `Rainy_Days`                       |                                    | Rainy Days                       |        |      sh2                            |
| `ndm`                              | `ndm`                              | `Normalized_Dry_Matter`            |                                    | National Drought Model           | kg_ha  |      sh2  sh3                       |
| `lai`                              | `lai`                              | `LAI`                              |                                    | Leaf Area Index                  | m2-m-2 |      sh2                            |
| `bf`                               | `bf`                               |                                    |                                    | Baseflow                         |        |                                     |
| `sr`                               | `sr`                               | `Surface_Runoff`                   |                                    | Surface Runoff                   |        |                     sh5             |
| `dro`                              | `dro`                              |                                    |                                    | Incremental Runoff               |        |                                     |
| `tr`                               | `tr`                               |                                    |                                    | Total Runoff                     |        |                     WPx             |
| `perc`                             | `perc`                             |                                    |                                    | Percolation                      |        |                                     |
| `dperc`                            | `dperc`                            |                                    |                                    | Incremental Percolation          |        |                                     |
|                                    |                                    | `Total_Supply_Surface_Water`       |                                    | Total Supply Surface Water       |        |                                     |
|                                    |                                    | `Total_Supply_Ground_Water`        |                                    | Total Supply Ground Water        |        |                                     |
| `supply`                           | `supply`                           | `Total_Supply`                     |                                    | Supply                           |        |                sh4  WPx             |
|                                    |                                    | `Non_Consumed_Water`               |                                    | Non Consumed Water               |        |                sh4                  |
|                                    |                                    | `NDVI`                             |                                    | NDVI                             |        |           sh3                       |
|                                    |                                    | `Non_Recovable_Flow_Ground_Water`  |                                    | Non Recovable Flow Ground Water  |        |                sh4                  |
|                                    |                                    | `Non_Recovable_Flow_Surface_Water` |                                    | Non Recovable Flow Surface Water |        |                sh4                  |
|                                    |                                    | `Recovable_Flow_Ground_Water`      |                                    | Recovable Flow Ground Water      |        |                sh4                  |
|                                    |                                    | `Recovable_Flow_Surface_Water`     |                                    | Recovable Flow Surface Water     |        |                sh4                  |
|                                    |                                    | `Non_Recovable_Flow`               |                                    | Non Recovable Flow               |        |                sh4                  |
|                                    |                                    | `Recovable_Flow`                   |                                    | Recovable Flow                   |        |                sh4                  |
|                                    |                                    | `Surface_Withdrawal`               |                                    | Surface Withdrawal               |        |                     sh5             |

_Template 2D variable_

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
                dtype=np.float32
        )
```

_Template 3D variable_

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

Some templates and standards can be found in 
[IHEWAstandard/resources/Products.xlsx](https://github.com/wateraccounting/IHEWAstandard/tree/master/resources).

Archived Data

  - [Archived Engine.Data.Engine1](./Archived-Data.md#engine-1)
  - [Archived Engine.Data.Engine2](./Archived-Data.md#engine-2)


# [Examples](examples/README.md#data)
