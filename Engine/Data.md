# IHEWAstandard.Engine.Data

Define the **Engine.Data standard** of WaterAccounting Tools.

**TOC**

  - [Standard](#standard)
    - [File name](#file-name)
    - [Attributes/Metadata](#attributesmetadata)
    - [Dimensions](#dimensions)
    - [Coordinates variables](#coordinates-variables)
    - [Data variables](#data-variables)
      - [CRS](#crs)
      - [Variables](#variables)
  - [Resources](#resources)
  - [Examples](#examples)


## Standard

Example, [watools.General.data_convertions.Save_as_NC()](https://github.com/wateraccounting/watools/blob/master/General/data_conversions.py#L279)

### File name

| Template                 | Example                                                            | Remarks |
| -----------------------: | ------------------------------------------------------------------ | ------- |
| Engine2.Input.Day.nc     | `EngineNumber`.`Input/Output`.`TemporalResolution`.`FileExtension` |         |

> The following template use '**day**' as temporal resolution.

### Attributes/Metadata

Attributes, Metadata
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

Dimensions
> inculded in NetCDF file

time, y, x => time, lat, lon

_Template_

```Python
'dims': ('time', 'y', 'x')
```

### Coordinates variables

Coordinates
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

#### CRS

Coordinate Reference System
> inculded in NetCDF file
> 
> **DO NOT CHANGE 'crs'!**

_Template_

```Python
'crs': {                                        # variable short name, 'crs': 'EPSG:4326 - WGS 84 - Geographic'
        'dims': (),
        'attrs': {
                'standard_name':                'coordinate_reference_system',
                'long_name':                    'Lon/Lat Coords in WGS84',
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

#### Variables

Parameter, **csv** data
> not inculded in NetCDF file

| Variable Name/Code                 | Standard Name                | units  | Sheet                               | Other |
| ---------------------------------: | ---------------------------- | ------ | ----------------------------------- | ----- |
| **0D, Parameter**                                                                                                        |
| `name`                             | Basin name VGTB              |        | sh1I sh2I sh3I sh4I sh5I sh6I sh7I  | metadata |
| `recycling_ratio`                  | Ratio                        |        | sh1I                          sh7I  | metadata|
| `water_year_start_month`           | Start month of water year    |        | sh1I           sh4I sh5I sh6I sh7I  | metadata |
| `surfwat`                          |                              |        |                     sh5I            | metadata |
| `discharge_natural`                |                              |        |                     sh5I            | surfwat |
| `discharge_end`                    |                              |        |                     sh5I            | surfwat |
| **0D, Extra**                                                                                                            |
| `grace`                            | GRACE                        |        |                                     |       |
| `grace_supply_split`               | GRACE                        |        |                sh4I                 |       |
| `grace_split_alpha_bounds`         | GRACE                        |        |                                     |       |
| `ndm_max_original`                 | National Drought Model       |        |                                     |       |
| **1D, Parameter**                                                                                                        |
| `dico_in`                          | subbasin in or outflow point |        |                     sh5I            | metadata |
| `dico_out`                         | subbasin in or outflow point |        |                     sh5I            | metadata |
| `fraction_xs`                      | Fraction Altitude XS         |        |                     sh5I            | metadata |
| **1D, Calendar**                                                                                                         |
| Crops, Sheet 3, metadata                                                                                                 |
| `rice-rainfed`                     | Crops Cereals                |        |                                     |       |
| `rice-irrigated`                   | Crops Cereals                |        |                                     |       |
| `tea`                              | Crops Beverage crops         |        |                                     |       |
| `fodder`                           | Crops Other crops            |        |                                     |       |
| `sugar cane`                       | Crops Non-cereals            |        |                                     |       |
| Non-Crops, Sheet 3, metadata                                                                                             |
| `meat`                             | Non-Crops STATS_GSOV         |        |                                     |       |
| `milk`                             | Non-Crops STATS_GSOV         |        |                                     |       |
| `timber`                           | Non-Crops STATS_GSOV         |        |                                     |       |
| `aquaculture`                      | Non-Crops STATS_GSOV         |        |                                     |       |

GIS, **NetCDF** data
> inculded in NetCDF file

  - **Variables Name**: All upper characters.
  - **Standard name**: lower characters with underscore for white space.
  - **Long name**: First upper character with white space.

Data category, the idea is based on **SWAT+** Input/Output [Documentation](../resources/Products-TWRI-swat2012_io_documentation.pdf) and FAO **WaPOR** [Database](../resources/Products.xlsx).

| Variables Name/Code | Standard Name                                    | Long Name                                        | Sheet Input                         | Sheet Output                        | Other |
| ------------------: | ------------------------------------------------ | ------------------------------------------------ | ----------------------------------- | ----------------------------------- | ----- |
| `AB`                | aa_bb                                            | Aa Bb                                            |  1,   2,   3,   4,   5,   6,   7,   |  1,   2,   3,   4,   5,   6,   7,   |       |
| **Basin** |
| ~~`BSN`~~           | basin                                            | Basin                                            |                                     |                                     |       |
| ~~`SUB`~~           | subbasin                                         | Subbasin                                         |                                     |                                     |       |
| `DEM`               | digital_elevation_model                          | Digital Elevation Model                          |                                     |                                     |       |
| `DIR`               | drainage_direction_model                         | Drainage Direction Model                         |                                     |                                     |       |
| **Land** |
| `LU`                | landuse_landcover                                | Landuse Landcover                                |                                     |                                     |       |
| **Canopy** |
| `LAI`               | leaf_area_index                                  | Leaf Area Index                                  |                                     |                                     |       |
| **Condensation** |
| **Precipitation** |
| `PCP`               | precipitation                                    | Precipitation                                    |                                     |                                     |       |
| `N`                 | rainy_days                                       | Rainy Days                                       |                                     |                                     |       |
| **Evapotranspiration** |
| `ET`, _`ETA`_       | evapotranspiration                               | Evapotranspiration                               |                                     |                                     |       |
| `ETR`               | reference_evapoTranspiration                     | Reference EvapoTranspiration                     |                                     |                                     |       |
| `ETP`               | potential_evapoTranspiration                     | Potential EvapoTranspiration                     |                                     |                                     |       |
| `ETB`               | blue_evapoTranspiration                          | Blue EvapoTranspiration                          |                                     |                                     |       |
| `ETG`               | green_evapoTranspiration                         | Green EvapoTranspiration                         |                                     |                                     |       |
| **Evaporation, from soil and surface-water bodies** |
| `E`                 | evaporation                                      | Evaporation                                      |                                     |                                     |       |
| **Interception, by vegetal cover or depression storage** |
| `I`                 | interception                                     | Interception                                     |                                     |                                     |       |
| **Transpiration, by biological process, plants is transferred from the plant to the atmosphere** |
| `T`                 | transpiration                                    | Transpiration                                    |                                     |                                     |       |
| **Infiltration, by soil** |
| **Percolation, Ground-water recharge** |
| `PERC`              | percolation                                      | Percolation                                      |                                     |                                     |       |
| `DPERC`             | incremental_percolation                          | Incremental Percolation                          |                                     |                                     |       |
| **Ground-water discharge** |
| `BF`                | baseflow                                         | Baseflow                                         |                                     |                                     |       |
| **Storage, by planetary water cycle** |
| **Irrigation** |
| `RF`                | return_flow                                      | Return Flow                                      |                                     |                                     |       |
| **Runoff, from rainfall and snowmelt** |
| `TR`                | total_runoff                                     | Total Runoff                                     |                                     |                                     |       |
| `SR`                | surface_runoff                                   | Surface Runoff                                   |                                     |                                     |       |
| `DRO`               | incremental_runoff                               | Incremental Runoff                               |                                     |                                     |       |
| **Draught** |
| `NDM`               | national_drought_model                           | National Drought Model                           |                                     |                                     |       |
| **Supply** |
| `SUPPLY`            | supply                                           | Supply                                           |                                     |                                     |       |
| **Population** |
| `POP`               | population                                       | Population                                       |                                     |                                     |       |


_Variable Name, Input/Output, Map_

| Variables Name/Code                | Hyperloop                          | watools                            | WaPOR                              | Long Name                        | units  | Sheet                               | Script |
| ---------------------------------: | ---------------------------------- | ---------------------------------- | ---------------------------------- | -------------------------------- | ------ | ----------------------------------- | ----- |
| **2D, Static Map** |
| Integer           |
| `LU`                               | `lu`                               | `Landuse`                          | `LCC`                              | VGTB                             |        | sh1I sh2I sh3I sh4I sh5I sh6I sh7I  | metadata |
| `full_basin_mask`                  | `full_basin_mask`                  |                                    |                                    | VGTB                             |        |                                     |       |
| `masks`                            | `masks`                            |                                    |                                    | VGTB                             |        |                     sh5I            | metadata |
| `POP`                              | `population_tif`                   |                                    |                                    | VNM-POP VNM_pph_v2b_2009         |        |                sh4I           sh7   | global_data |
| Float                                                                                                                                                                                                                                       |
|                                    |                                    | `Water_Occurrence`                 |                                    | Water Occurrence                 |        |                     WPx             |       |
| `DEM`                              | `dem`                              |                                    |                                    | Elevation Void-filled            |        |                     sh5I            | global_data |
| `DIR`                              | `dir`                              |                                    |                                    | Direction Drainage               |        |                     sh5             |       |
| `equiped_sw_irrigation`            | `equiped_sw_irrigation`            |                                    |                                    | GMIA FAO                         |        |                sh4I                 |       |
| `environ_water_req`                | `environ_water_req`                |                                    |                                    | EF EWR                           |        | sh1I                sh5I            | global_data |
| `WPL`                              | `wpl_tif`                          | `Grey_Water_Footprint`             |                                    | Grey Water Footprint             |        | sh1I           sh4I sh5I            | global_data |
|                                    |                                    | `Theta_Saturated_Topsoil`          |                                    | Theta Saturated Topsoil          |        |               _sh4_                 |       |
| `fractions`                        | `fractions`                        | `Fraction_Surface_Water_Supply`    |                                    | Fractions, Surface Water Supply  |        | sh1I           sh4I sh5O sh6I       | complete_data, `sw_supply_fraction.tif`, `fractions_altitude.tif` |
| **3D, Timeserise Map** |
| `PCP`                              | `p`                                | `Precipitation`                    | `PCP`                              | Precipitation                    | mm     | sh1I sh2I sh3I sh4I sh5I      sh7   | complete_data |
|                                    |                                    | `Evaporation`                      |                                    | Evaporation                      |        |     _sh2_                           |       |
| `T`                                | `t`                                | `Transpiration`                    |                                    | Transpiration                    |        |      sh2I                           | complete_data |
| `I`                                | `i`                                | `Interception`                     |                                    | Interception                     |        |      sh2I                           | complete_data |
| `ETB`                              | `etb`                              | `Blue_Evapotranspiration`          |                                    | Blue EvapoTranspiration          |        | sh1I      sh3I sh4I      sh6I sh7   | complete_data, `conventional_et`, `CONSUMED_ET` |
| `ETG`                              | `etg`                              | `Green_Evapotranspiration`         |                                    | Green EvapoTranspiration         |        | sh1I      sh3I_sh4_           sh7   | complete_data |
| `ETP`                              | `pet`                              |                                    |                                    | Potential EvapoTranspiration     | mm     |                                     |       |
| `ETR`                              | `etref`                            | `Reference_Evapotranspiration`     | `RET`                              | Reference EvapoTranspiration     |        |          _sh3_ sh4I_sh5_            | complete_data |
| `ET`                               | `et`                               | `Actual_Evapotranspiration`        |                                    | Actual EvapoTranspiration        |        |      sh2I_sh3_ sh4I_sh5_            | complete_data |
| `N`                                | `n`                                | `Rainy_Days`                       |                                    | Rainy Days                       |        |      sh2I                           | complete_data |
|                                    |                                    | `NDVI`                             |                                    | NDVI                             |        |          _sh3_                      |       |
| `NDM`                              | `ndm`                              | `Normalized_Dry_Matter`            |                                    | National Drought Model           | kg_ha  |      sh2I sh3I                sh7   | complete_data |
| `LAT`                              | `lai`                              | `LAI`                              |                                    | Leaf Area Index                  | m2-m-2 |      sh2I      sh4I                 | complete_data |
| `BF`                               | `bf`                               |                                    |                                    | Baseflow                         |        |                sh4I sh5I sh6I sh7   | complete_data |
| `SR`                               | `sr`                               | `Surface_Runoff`                   |                                    | Surface Runoff                   |        |                     sh5I            | complete_data |
| `DRO`                              | `dro`                              |                                    |                                    | Incremental Runoff               |        |                sh4I      sh6I       | complete_data, `non_consumed_dsro` |
| `TR`                               | `tr`                               |                                    |                                    | Total Runoff                     |        | sh1I                sh5I      sh7   | complete_data |
| `PERC`                             | `perc`                             |                                    |                                    | Percolation                      |        |                          sh6I       | complete_data. `non_consumed_dperc` |
| `DPERC`                            | `dperc`                            |                                    |                                    | Incremental Percolation          |        |                sh4I      sh6I       | complete_data |
|                                    | `recharge`                         |                                    |                                    |                                  |        |                          sh6O       | complete_data, `recharge_tif`, `VERTICAL_RECHARGE` |
|                                    | `supply_swa`                       |                                    |                                    |                                  |        |                          sh6O       | complete_data, `supply_swa` |
|                                    | `supply_sw`                        | `Total_Supply_Surface_Water`       |                                    | Total Supply Surface Water       |        |                sh4O sh5I            | complete_data, `supply_sw_tif`, `SUPPLY_SURFACEWATER`, `VERTICAL_GROUNDWATER_WITHDRAWALS` |
|                                    | `supply_gw`                        | `Total_Supply_Ground_Water`        |                                    | Total Supply Ground Water        |        |                sh4O      sh6IO      | complete_data, `supply_gw_tif`, `SUPPLY_GROUNDWATER` |
| `SUPPLY`                           | `supply_total`                     | `Total_Supply`                     |                                    | Supply                           |        |                sh4I      sh6I       | complete_data,`total_supply_tif` |
|                                    | ` `                                | ` `                                |                                    | Non Consumed Surface Water       |        |                          sh6O       | `non_consumed_sw_tif` |
|                                    | ` `                                | ` `                                |                                    | Non Consumed Ground Water        |        |                          sh6O       | `non_consumed_gw_tif` |
|                                    | ` `                                | `Non_Consumed_Water`               |                                    | Non Consumed Water               |        |                sh4O      sh6O       | `non_consumed_tif` |
|                                    | ` `                                | `Non_Recovable_Flow_Surface_Water` |                                    | Non Recovable Flow Surface Water |        |                sh4O                 | `non_recov_sw_tif`, `RECOVERABLE_GROUNDWATER` |
|                                    | ` `                                | `Non_Recovable_Flow_Ground_Water`  |                                    | Non Recovable Flow Ground Water  |        |                sh4O                 | `non_recov_gw_tif`, `NON_RECOVERABLE_GROUNDWATER` |
|                                    | ` `                                | `Non_Recovable_Flow`               |                                    | Non Recovable Flow               |        |                sh4O                 | `non_recov_tif` |
|                                    | ` `                                | `Recovable_Flow_Surface_Water`     |                                    | Recovable Flow Surface Water     |        |                sh4O                 | `recov_sw_tif`, `RECOVERABLE_SURFACEWATER` |
|                                    | ` `                                | `Recovable_Flow_Ground_Water`      |                                    | Recovable Flow Ground Water      |        |                sh4O                 | `recov_gw_tif`, `RECOVERABLE_GROUNDWATER` |
|                                    | ` `                                | `Recovable_Flow`                   |                                    | Recovable Flow                   |        |                sh4O                 | `recov_tif` |
|                                    | `return_flow_sw_sw`                |                                    |                                    |                                  |        |                     sh5I sh6O       | complete_data, `return_flow_sw_sw_tif` |
|                                    | `return_flow_sw_gw`                |                                    |                                    |                                  |        |                          sh6O       | complete_data, `return_flow_sw_gw_tif` |
|                                    | `return_flow_gw_sw`                |                                    |                                    |                                  |        |                     sh5I sh6O       | complete_data, `return_flow_gw_sw_tif` |
|                                    | `return_flow_gw_gw`                |                                    |                                    |                                  |        |                          sh6O       | complete_data, `return_flow_gw_gw_tif` |
|                                    | `withdrawls`                       | `Surface_Withdrawal`               |                                    | Surface Withdrawal               |        |                     sh5O            |       |

_Variable Name, Calculation/HYD Processes, Script_

| Variables Name/Code                | Hyperloop                          | watools                            | WaPOR                              | Standard Name                    | units  | Sheet                               | Script |
| ---------------------------------: | ---------------------------------- | ---------------------------------- | ---------------------------------- | -------------------------------- | ------ | ----------------------------------- | ----- |
| **Sheet 1** |
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
| **Sheet 5** |
|                                    | total_outflow                      |                                    |                                    |                                  |        |                     sh5             | results |
|                                    | non_recoverable_outflow            |                                    |                                    |                                  |        |                     sh5             | results |
|                                    | non_utilizable_outflow             |                                    |                                    |                                  |        |                     sh5             | results |
|                                    | committed_outflow                  |                                    |                                    |                                  |        |                     sh5             | results |
|                                    | utilizable_outflow                 |                                    |                                    |                                  |        |                     sh5             | results |
|                                    | deltaS                             |                                    |                                    |                                  |        |                     sh5             | results |
|                                    | interbasin_transfers               |                                    |                                    |                                  |        |                     sh5             | results |
|                                    | inflows                            |                                    |                                    |                                  |        |                     sh5             | results |
|                                    | surf_runoff                        |                                    |                                    |                                  |        |                     sh5             | results |
|                                    | base_runoff                        |                                    |                                    |                                  |        |                     sh5             | results |
|                                    | total_runoff                       |                                    |                                    |                                  |        |                     sh5             | results |
|                                    | withdrawls                         |                                    |                                    |                                  |        |                     sh5             | results |
|                                    | return_gw_sw                       |                                    |                                    |                                  |        |                     sh5             | results |
|                                    | return_sw_sw                       |                                    |                                    |                                  |        |                     sh5             | results |
| **Sheet 7** |
|                                    | cattle                             |                                    |                                    |                                  |        |                               sh7   | global_data |
|                                    | root_depth                         |                                    |                                    |                                  |        |                               sh7   | global_data |
|                                    | recharge                           |                                    |                                    |                                  |        |                               sh7   | complete_data |
|                                    | rzsm                               |                                    |                                    |                                  |        |                               sh7   | complete_data |
|                                    | tot_runoff                         |                                    |                                    |                                  |        |                               sh7   | results |
|                                    | feed_incremental                   |                                    |                                    |                                  |        |                               sh7   | results |
|                                    | feed_landscape                     |                                    |                                    |                                  |        |                               sh7   | results |
|                                    | fuel_incremental                   |                                    |                                    |                                  |        |                               sh7   | results |
|                                    | fuel_landscape                     |                                    |                                    |                                  |        |                               sh7   | results |
|                                    | baseflow                           |                                    |                                    |                                  |        |                               sh7   | results |
|                                    | gw_rech                            |                                    |                                    |                                  |        |                               sh7   | results |
|                                    | root_storage                       |                                    |                                    |                                  |        |                               sh7   | results |
|                                    | atm_recycl_landscape               |                                    |                                    |                                  |        |                               sh7   | results |
|                                    | atm_recycl_incremental             |                                    |                                    |                                  |        |                               sh7   | results |
|                                    | # fish                             |                                    |                                    |                                  |        |                               sh7   | results |


_Template 2D variable_

```Python
'DEM': {
        'dims': (                               # variable dimensions, 2D
                'y',
                'x'
        ),
        'attrs': {                              # variable attributes
                                                # 'grid_mapping' linked with variable 'crs'
                'grid_mapping':  'crs',
                'standard_name': 'digital_elevation_model',
                'long_name':     'Digital Elevation Model',
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
'PCP': {                                        # variable short name
        'dims': (                               # variable dimensions
                'time',
                'y',
                'x'
        ),
        'attrs': {                              # variable attributes
                'grid_mapping':  'crs',         # 'grid_mapping' linked with variable 'crs'
                'standard_name': 'precipitation',
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
