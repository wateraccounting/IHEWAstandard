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

| Variable Name/Code                 | Standard Name                | units  | Sheet                          | Other |
| ---------------------------------: | ---------------------------- | ------ | ------------------------------ | ----- |
| **0D, Parameter**                                                                                                   |
| `name`                             | Basin name VGTB              |        | sh1  sh2  sh3                  | metadata |
| `recycling_ratio`                  | Ratio                        |        | sh1                            |       |
| `water_year_start_month`           | Start month of water year    |        | sh1                 sh5        |       |
| **0D, Extra**                                                                                                       |
| `grace`                            | GRACE                        |        |                                |       |
| `grace_supply_split`               | GRACE                        |        |                sh4             |       |
| `grace_split_alpha_bounds`         | GRACE                        |        |                                |       |
| `ndm_max_original`                 | National Drought Model       |        |                                |       |
| **1D, Parameter**                                                                                                   |
| `dico_in`                          | subbasin in or outflow point |        |                     sh5        | metadata |
| `dico_out`                         | subbasin in or outflow point |        |                     sh5        | metadata |
| `fraction_xs`                      | Fraction                     |        |                     sh5        |       |
| **1D, Calendar**                                                                                                    |
| Crops, Sheet 3, metadata                                                                                            |
| `rice-rainfed`                     | Crops Cereals                |        |                                |       |
| `rice-irrigated`                   | Crops Cereals                |        |                                |       |
| `tea`                              | Crops Beverage crops         |        |                                |       |
| `fodder`                           | Crops Other crops            |        |                                |       |
| `sugar cane`                       | Crops Non-cereals            |        |                                |       |
| Non-Crops, Sheet 3, metadata                                                                                        |
| `meat`                             | Non-Crops STATS_GSOV         |        |                                |       |
| `milk`                             | Non-Crops STATS_GSOV         |        |                                |       |
| `timber`                           | Non-Crops STATS_GSOV         |        |                                |       |
| `aquaculture`                      | Non-Crops STATS_GSOV         |        |                                |       |

GIS data

> inculded in NetCDF file

| Variables Name/Code                | Hyperloop                          | watools                            | WaPOR                              | Standard Name                    | units  | Sheet                               | Other |
| ---------------------------------: | ---------------------------------- | ---------------------------------- | ---------------------------------- | -------------------------------- | ------ | ----------------------------------- | ----- |
| **2D, Static Map**                                                                                                                                                                                                                          |
| Integer                                                                                                                                                                                                                                     |
| `lu`                               | `lu`                               | `Landuse`                          | `LCC`                              | VGTB                             |        | sh1  sh2  sh3  sh4  sh5             | metadata |
| `full_basin_mask`                  | `full_basin_mask`                  |                                    |                                    | VGTB                             |        |                                     |       |
| `masks`                            | `masks`                            |                                    |                                    | VGTB                             |        |                     sh5             | metadata |
| `population_tif`                   | `population_tif`                   |                                    |                                    | VNM-POP VNM_pph_v2b_2009         |        |                sh4                  | global_data |
| Float                                                                                                                                                                                                                                       |
|                                    |                                    | `Water_Occurrence`                 |                                    | Water Occurrence                 |        |                     WPx             |       |
| `dem`                              | `dem`                              |                                    |                                    | Elevation                        |        |                     sh5             | global_data |
| `dir`                              | `dir`                              |                                    |                                    | Direction                        |        |                     sh5             |       |
| `equiped_sw_irrigation`            | `equiped_sw_irrigation`            |                                    |                                    | GMIA FAO                         |        |                sh4                  |       |
| `environ_water_req`                | EWR: `environ_water_req`           |                                    |                                    | EF EWR                           |        | sh1                 sh5             | global_data |
| `wpl_tif`                          | WPL: `wpl_tif`                     | `Grey_Water_Footprint`             |                                    | Grey Water Footprint             |        | sh1            sh4  sh5             | global_data |
|                                    |                                    | `Theta_Saturated_Topsoil`          |                                    | Theta Saturated Topsoil          |        |                sh4                  |       |
|                                    |                                    | `Fraction_Surface_Water_Supply`    |                                    | Fraction Surface Water Supply    |        |                     sh5             |       |
| `fractions`                        | Fractions: `fractions`             |                                    |                                    | Fractions                        |        | sh1                 sh5             | complete_data |
| **3D, Timeserise Map**                                                                                                                                                                                                                      |
| `pcp`                              | P: `p`                             | `Precipitation`                    | `PCP`                              | Precipitation                    | mm     | sh1  sh2  sh3  sh4  sh5             | complete_data |
|                                    |                                    | `Evaporation`                      |                                    | Evaporation                      |        |      sh2                            |       |
|                                    | `t`                                | `Transpiration`                    |                                    | Transpiration                    |        |      sh2                            | complete_data |
|                                    | `i`                                | `Interception`                     |                                    | Interception                     |        |      sh2                            | complete_data |
| `pet`                              | `pet`                              |                                    |                                    | Potential EvapoTranspiration     | mm     |                                     |       |
| `ret`                              | `etref`                            | `Reference_Evapotranspiration`     | `RET`                              | Reference EvapoTranspiration     |        |          _sh3_ sh4  sh5             | complete_data |
| `aet`                              |                                    | `Actual_Evapotranspiration`        |                                    | Actual EvapoTranspiration        |        |      sh2 _sh3_ sh4 _sh5_            |       |
| `bet`                              | ETblue: `etb`                      | `Blue_Evapotranspiration`          |                                    | Blue EvapoTranspiration          |        | sh1       sh3  sh4                  | complete_data |
| `get`                              | ETgreen: `etg`                     | `Green_Evapotranspiration`         |                                    | Green EvapoTranspiration         |        | sh1       sh3 _sh4_                 | complete_data |
| `et`                               | `et`                               |                                    |                                    | Evapotranspiration               |        |      sh2                            | complete_data |
| `n`                                | `n`                                | `Rainy_Days`                       |                                    | Rainy Days                       |        |      sh2                            | complete_data |
|                                    |                                    | `NDVI`                             |                                    | NDVI                             |        |          _sh3_                      |       |
| `ndm`                              | `ndm`                              | `Normalized_Dry_Matter`            |                                    | National Drought Model           | kg_ha  |      sh2  sh3                       | complete_data |
| `lai`                              | `lai`                              | `LAI`                              |                                    | Leaf Area Index                  | m2-m-2 |      sh2       sh4                  | complete_data |
| `bf`                               | base_runoff: `bf`                  |                                    |                                    | Baseflow                         |        |                sh4  sh5             | complete_data |
| `sr`                               | surf_runoff: `sr`                  | `Surface_Runoff`                   |                                    | Surface Runoff                   |        |                     sh5             | complete_data |
| `dro`                              | `dro`                              |                                    |                                    | Incremental Runoff               |        |                sh4                  | complete_data |
| `tr`                               | total_runoff: `tr`                 |                                    |                                    | Total Runoff                     |        | sh1                 sh5             | complete_data |
| `perc`                             | `perc`                             |                                    |                                    | Percolation                      |        |                sh4                  | complete_data |
| `dperc`                            | `dperc`                            |                                    |                                    | Incremental Percolation          |        |                sh4                  | complete_data |
|                                    | `supply_sw`                        | `Total_Supply_Surface_Water`       |                                    | Total Supply Surface Water       |        |                sh4  sh5             | complete_data |
|                                    | `supply_gw`                        | `Total_Supply_Ground_Water`        |                                    | Total Supply Ground Water        |        |                sh4                  | complete_data |
| `supply`                           | `supply_total`                     | `Total_Supply`                     |                                    | Supply                           |        |                sh4                  |       |
|                                    |                                    | `Non_Consumed_Water`               |                                    | Non Consumed Water               |        |                sh4                  |       |
|                                    |                                    | `Non_Recovable_Flow_Ground_Water`  |                                    | Non Recovable Flow Ground Water  |        |                sh4                  |       |
|                                    |                                    | `Non_Recovable_Flow_Surface_Water` |                                    | Non Recovable Flow Surface Water |        |                sh4                  |       |
|                                    |                                    | `Recovable_Flow_Ground_Water`      |                                    | Recovable Flow Ground Water      |        |                sh4                  |       |
|                                    |                                    | `Recovable_Flow_Surface_Water`     |                                    | Recovable Flow Surface Water     |        |                sh4                  |       |
|                                    |                                    | `Non_Recovable_Flow`               |                                    | Non Recovable Flow               |        |                sh4                  |       |
|                                    |                                    | `Recovable_Flow`                   |                                    | Recovable Flow                   |        |                sh4                  |       |
|                                    | withdrawls:                        | `Surface_Withdrawal`               |                                    | Surface Withdrawal               |        |                     sh5             |       |

| Variables Name/Code                | Hyperloop                          | watools                            | WaPOR                              | Standard Name                    | units  | Sheet                               | Other |
| ---------------------------------: | ---------------------------------- | ---------------------------------- | ---------------------------------- | -------------------------------- | ------ | ----------------------------------- | ----- |
| **Sheet 1**                                                                                                                                                                                                                         |
|                                    | et_advection                       |                                    |                                    |                                  |        | sh1                                 | results |
|                                    | p_advection                        |                                    |                                    |                                  |        | sh1                                 | results |
|                                    | p_recycled                         |                                    |                                    |                                  |        | sh1                                 | results |
|                                    | dS                                 |                                    |                                    |                                  |        | sh1                                 | results |
|                                    | non_recoverable                    |                                    |                                    |                                  |        | sh1                                 | results |
|                                    | reserved_outflow_demand            |                                    |                                    |                                  |        | sh1                                 | results |
|                                    | other                              |                                    |                                    |                                  |        | sh1                                 | results |
|                                    | manmade                            |                                    |                                    |                                  |        | sh1                                 | results |
|                                    | natural                            |                                    |                                    |                                  |        | sh1                                 | results |
|                                    | uf_plu                             |                                    |                                    |                                  |        | sh1                                 | results |
|                                    | uf_ulu                             |                                    |                                    |                                  |        | sh1                                 | results |
|                                    | uf_mlu                             |                                    |                                    |                                  |        | sh1                                 | results |
|                                    | uf_mwu                             |                                    |                                    |                                  |        | sh1                                 | results |
|                                    | non_utilizable_outflow             |                                    |                                    |                                  |        | sh1                                 | results |
|                                    | reserved_outflow_actual            |                                    |                                    |                                  |        | sh1                                 | results |
|                                    | utilizable_outflow                 |                                    |                                    |                                  |        | sh1                                 | results |
|                                    | landscape_et_mwu                   |                                    |                                    |                                  |        | sh1                                 | results |
|                                    | landscape_et_mlu                   |                                    |                                    |                                  |        | sh1                                 | results |
|                                    | landscape_et_ulu                   |                                    |                                    |                                  |        | sh1                                 | results |
|                                    | landscape_et_plu                   |                                    |                                    |                                  |        | sh1                                 | results |
|                                    | q_outflow                          |                                    |                                    |                                  |        | sh1                                 | results |
|                                    | q_in_sw                            |                                    |                                    |                                  |        | sh1                                 | results |
|                                    | q_in_gw                            |                                    |                                    |                                  |        | sh1                                 | results |
|                                    | q_in_desal                         |                                    |                                    |                                  |        | sh1                                 | results |
|                                    | q_out_sw                           |                                    |                                    |                                  |        | sh1                                 | results |
|                                    | q_out_gw                           |                                    |                                    |                                  |        | sh1                                 | results |
| **Sheet 4_6**                                                                                                                                                                                                                       |
|                                    | recharge                           |                                    |                                    |                                  |        |                sh4                  | complete_data |
|                                    | supply_swa                         |                                    |                                    |                                  |        |                sh4                  | complete_data |
|                                    | return_flow_sw_sw                  |                                    |                                    |                                  |        |                sh4                  | complete_data |
|                                    | return_flow_sw_gw                  |                                    |                                    |                                  |        |                sh4                  | complete_data |
|                                    | return_flow_gw_sw                  |                                    |                                    |                                  |        |                sh4                  | complete_data |
|                                    | return_flow_gw_gw                  |                                    |                                    |                                  |        |                sh4                  | complete_data |
| **Sheet 5**                                                                                                                                                                                                                         |
|                                    | return_flow_gw_sw                  |                                    |                                    |                                  |        |                     sh5             | complete_data |
|                                    | return_flow_sw_sw                  |                                    |                                    |                                  |        |                     sh5             | complete_data |
|                                    | total_outflow                      |                                    |                                    |                                  |        |                     sh5             | results |
|                                    | committed_outflow                  |                                    |                                    |                                  |        |                     sh5             | results |
|                                    | non_utilizable_outflow             |                                    |                                    |                                  |        |                     sh5             | results |
|                                    | utilizable_outflow                 |                                    |                                    |                                  |        |                     sh5             | results |
|                                    | non_recoverable_outflow            |                                    |                                    |                                  |        |                     sh5             | results |
|                                    | deltaS                             |                                    |                                    |                                  |        |                     sh5             | results |
|                                    | interbasin_transfers               |                                    |                                    |                                  |        |                     sh5             | results |
|                                    | inflows                            |                                    |                                    |                                  |        |                     sh5             | results |
|                                    | surf_runoff                        |                                    |                                    |                                  |        |                     sh5             | results |
|                                    | base_runoff                        |                                    |                                    |                                  |        |                     sh5             | results |
|                                    | total_runoff                       |                                    |                                    |                                  |        |                     sh5             | results |
|                                    | withdrawls                         |                                    |                                    |                                  |        |                     sh5             | results |
|                                    | return_gw_sw                       |                                    |                                    |                                  |        |                     sh5             | results |
|                                    | return_sw_sw                       |                                    |                                    |                                  |        |                     sh5             | results |


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
