# IHEWAstandard.Engine.Data

Define the **Engine.Data standard** of WaterAccounting Tools.

**TOC**

  - [Standard](#standard)
  - [Resources](#resources)
  - [Engine 1](#engine-1)
    - [Input, NetCDF](#engine-1-input-netcdf)
    - [Output, NetCDF](#engine-1-output-netcdf)
  - [Engine 2](#engine-2)
    - [Input, NetCDF](#engine-2-input-netcdf)
    - [Output, CSV](#engine-2-output-csv)
  - [Examples](#examples)


## Standard

### File name

| Template                 | Example                                                            | Remarks |
| -----------------------: | ------------------------------------------------------------------ | ------- |
| Engine2.Input.Monthly.nc | `EngineNumber`.`Input/Output`.`TemporalResolution`.`FileExtension` |         |

### Metadata/Attributes

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
| rasterW        | Double | 10.0              | Raster Width                                                |
| rasterH        | Double | -10.0             | Raster Height                                               |

### Dimensions

```Python
('time', 'y', 'x')
```

### Coordinates variables

```Python
'lon': {                                            # longitude,    np.ndarray
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
'lat': {                                            # latitude,    np.ndarray
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
```

### Data variables

#### Coordinate Reference System, **DO NOT CHANGE 'crs'!**

Example python:

```Python
'crs': {                                            # variable short name, 'crs': 'EPSG:4326 - WGS 84 - Geographic'
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
        'data': np.NaN
}
```

#### Hydrological Variables

| Variable Name/Code | Standard Name | units  | Description                                                |
| -----------------: | ------------- | ------ | ---------------------------------------------------------- |
| `pcp`              | Precipitation | mm/day | The value of each pixel represents the total of daily precipitation in the year expressed in mm |
| `pet`              | Potential EvapoTranspiration | mm/day | The value of each pixel represents the total of daily Potential EvapoTranspiration in the year expressed in mm |

Example python:

```Python
'pcp': {                                            # variable short name
        'dims': (                                   # variable dimensions
                'time',
                'y',
                'x'
        ),
        'attrs': {                                  # variable attributes
                'grid_mapping':  'crs',             # # 'grid_mapping' linked with variable 'crs'
                'standard_name': 'Precipitation',
                'long_name':     'Precipitation',
                'units':         'mm/day',
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


## Engine 2

Example from Hyperloop.

### Engine 2, Input, NetCDF

  - `basins`, Define basin specific parameters
  - `global_data`, Define output folder and WaterPix file
  - `data`, Define paths of folders with temporal tif files

basins, {`ID`: metadata}

```Python
basins = {
  'ID': {
    'name':                     '',
    'lu':                       '',
    'full_basin_mask':          '',
    'masks':                    '',
    'crops':                    '',
    'non_crop':                 '',
    'recycling_ratio':          '',
    'dico_in':                  '',
    'dico_out':                 '',
    'GRACE':                    '',
    'fractioin_xs':             '',
    'discharge_out_from_wp':    '',
    'lu_based_supply_split':    '',
    'grace_supply_split':       '',
    'grace_split_alpha_bounds': '',
    'water_year_start_month':   '',
    'ndm_max_original':         ''
  }
}
```

global_data, {`variable_name`: path}

```Python
global_data = {
  'equiped_sw_irrigation':      'Landuse',
  'wpl':                        'Gray Water Footprint',
  'environ_water_req':          'EF',
  'population':                 'World population',
  'dem':                        'HydroSHED.DEM',
  'dir':                        'HydroSHED.DIR',
  'waterpix':                   'WaterPix'
}
```

data, {`folder_name`, path}

```Python
data = {
  'ndm':            'National Drought Model',
  'p':              'Precipitation',
  'et':             'Evapotranspiration',
  'n':              'Rainy Days',
  'lai':            'Leaf Area Index',
  'etref':          'Reference Evapotranspiration',
  'bf':             'Baseflow',
  'sr':             'Surface Runoff',
  'tr':             'Total Runoff',
  'perc':           'Percolation',
  'dperc':          'Incremental Percolation',
  'supply_total':   'Supply',
  'dro':            'Incremental Runoff',
  'etb':            'Blue Evapotranspiration',
  'etg':            'Green Evapotranspiration'
}
```

#### Dimensions

#### Variables of Dimension

#### Variables of Data


### Engine 2, Output, csv

#### Sheet 1

`create_sheet1()`

  - _Fractions_, `complete_data['fractions']`
  - _WPL_, `global_data["wpl_tif"]`
  - _EWR_, `global_data["environ_water_req"]`
  - _P_, `complete_data['p']`
  - _ETblue_, `complete_data['etb']`
  - _ETgreen_, `complete_data['etg']`

`create_csv()`

```Python
first_row = ['CLASS', 'SUBCLASS', 'VARIABLE', 'VALUE']

writer.writerow(['INFLOW',  'PRECIPITATION',    'Rainfall',                 '{0}'.format(results['p_advection'])])
writer.writerow(['INFLOW',  'PRECIPITATION',    'Snowfall',                 0.])
writer.writerow(['INFLOW',  'PRECIPITATION',    'Precipitation recycling',  '{0}'.format(results['p_recycled'])])
writer.writerow(['INFLOW',  'SURFACE WATER',    'Main riverstem',           '{0}'.format(results['q_in_sw'])])
writer.writerow(['INFLOW',  'SURFACE WATER',    'Tributaries',              0.])
writer.writerow(['INFLOW',  'SURFACE WATER',    'Utilized surface water',   0.])
writer.writerow(['INFLOW',  'SURFACE WATER',    'Flood',                    0.])
writer.writerow(['INFLOW',  'GROUNDWATER',      'Natural',                  '{0}'.format(results['q_in_gw'])])
writer.writerow(['INFLOW',  'GROUNDWATER',      'Utilized',                 0.])
writer.writerow(['INFLOW',  'OTHER',            'Desalinized',              '{0}'.format(results['q_in_desal'])])
writer.writerow(['STORAGE', 'CHANGE',           'Surface storage',          '{0}'.format(results['dS'])])
writer.writerow(['STORAGE', 'CHANGE',           'Storage in sinks',         0.])
writer.writerow(['OUTFLOW', 'ET LANDSCAPE',     'Protected',                '{0}'.format(results['landscape_et_plu'])])
writer.writerow(['OUTFLOW', 'ET LANDSCAPE',     'Utilized',                 '{0}'.format(results['landscape_et_ulu'])])
writer.writerow(['OUTFLOW', 'ET LANDSCAPE',     'Modified',                 '{0}'.format(results['landscape_et_mlu'])])
writer.writerow(['OUTFLOW', 'ET LANDSCAPE',     'Managed',                  '{0}'.format(results['landscape_et_mwu'])])
writer.writerow(['OUTFLOW', 'ET UTILIZED FLOW', 'Protected',                '{0}'.format(results['uf_plu'])])
writer.writerow(['OUTFLOW', 'ET UTILIZED FLOW', 'Utilized',                 '{0}'.format(results['uf_ulu'])])
writer.writerow(['OUTFLOW', 'ET UTILIZED FLOW', 'Modified',                 '{0}'.format(results['uf_mlu'])])
writer.writerow(['OUTFLOW', 'ET UTILIZED FLOW', 'Managed',                  '{0}'.format(results['uf_mwu'])])        
writer.writerow(['OUTFLOW', 'ET INCREMENTAL',   'Manmade',                  '{0}'.format(results['manmade'])])  
writer.writerow(['OUTFLOW', 'ET INCREMENTAL',   'Natural',                  '{0}'.format(results['natural'])])
writer.writerow(['OUTFLOW', 'SURFACE WATER',    'Main riverstem',           '{0}'.format(results['q_outflow'])])
writer.writerow(['OUTFLOW', 'SURFACE WATER',    'Tributaries',              0.])  
writer.writerow(['OUTFLOW', 'SURFACE WATER',    'Utilized surface water',   0.])  
writer.writerow(['OUTFLOW', 'SURFACE WATER',    'Flood',                    0.])
writer.writerow(['OUTFLOW', 'SURFACE WATER',    'Interbasin transfer',      '{0}'.format(results['q_out_sw'])])
writer.writerow(['OUTFLOW', 'GROUNDWATER',      'Natural',                  '{0}'.format(results['q_out_gw'])]) 
writer.writerow(['OUTFLOW', 'GROUNDWATER',      'Utilized',                 0.])
writer.writerow(['OUTFLOW', 'OTHER',            'Non-utilizable',           '{0}'.format(results['non_utilizable_outflow'])])
writer.writerow(['OUTFLOW', 'OTHER',            'Other',                    '{0}'.format(results['other'])])
writer.writerow(['OUTFLOW', 'RESERVED',         'Commited',                 '{0}'.format(results['reserved_outflow_actual'])]) 
writer.writerow(['OUTFLOW', 'RESERVED',         'Navigational',             0.]) 
writer.writerow(['OUTFLOW', 'RESERVED',         'Environmental',            0.]) 
```

#### Sheet 2

`create_sheet2_csv()`

  - _LAND_USE_,
  - _CLASS_,
  - _TRANSPIRATION_,
  - _WATER_,
  - _SOIL_,
  - _INTERCEPTION_,
  - _AGRICULTURE_,
  - _ENVIRONMENT_,
  - _ECONOMY_,
  - _ENERGY_,
  - _LEISURE_,
  - _NON_BENEFICIAL_,

```Python
first_row = ['LAND_USE', 'CLASS', 'TRANSPIRATION', 'WATER', 'SOIL', 'INTERCEPTION', 'AGRICULTURE', 'ENVIRONMENT', 'ECONOMY', 'ENERGY', 'LEISURE', 'NON_BENEFICIAL']

# Calculate evaporation.
E = ET - T - I

# Write data to csv-file.
for LAND_USE in classes_dict.keys():
    for CLASS in classes_dict[LAND_USE].keys():
        write_sheet2_row(LAND_USE, CLASS, lulc_dict, classes_dict, LULC, T, I, E, writer)
```

#### Sheet 3

**Sheet 3a**

`create_sheet3_csv()`

  - _USE_
  - _CLASS_
  - _SUBCLASS_
  - _TYPE_
  - _SUBTYPE_
  - _WATER_CONSUMPTION_

```Python
first_row_a = ["USE","CLASS","SUBCLASS","TYPE","SUBTYPE","WATER_CONSUMPTION"]

for TYPE in wp_y_rainfed_dictionary.keys():
    for SUBTYPE in wp_y_rainfed_dictionary[TYPE].keys():
        writer_a.writerow(["CROP",      "RAINFED",    "ET",            TYPE,SUBTYPE,"nan"])
for TYPE in wp_y_irrigated_dictionary.keys():
    for SUBTYPE in wp_y_irrigated_dictionary[TYPE].keys():
        writer_a.writerow(["CROP",      "IRRIGATED",  "ET rainfall",   TYPE,SUBTYPE,"nan"])
        writer_a.writerow(["CROP",      "IRRIGATED",  "Incremental ET",TYPE,SUBTYPE,"nan"])

for TYPE in wp_y_non_crop_dictionary.keys():
    for SUBTYPE in wp_y_non_crop_dictionary[TYPE].keys():
        writer_a.writerow(["NON-CROP",  "RAINFED",    "ET",            TYPE,SUBTYPE,"nan"])
        writer_a.writerow(["NON-CROP",  "IRRIGATED",  "ET rainfall",   TYPE,SUBTYPE,"nan"])
        writer_a.writerow(["NON-CROP",  "IRRIGATED",  "Incremental ET",TYPE,SUBTYPE,"nan"])
```

**Sheet 3b**

`create_sheet3_csv()`

  - _USE_
  - _CLASS_
  - _SUBCLASS_
  - _TYPE_
  - _SUBTYPE_
  - _LAND_PRODUCTIVITY_
  - _WATER_PRODUCTIVITY_

```Python
first_row_b = ["USE","CLASS","SUBCLASS","TYPE","SUBTYPE","LAND_PRODUCTIVITY","WATER_PRODUCTIVITY"]

for TYPE in wp_y_rainfed_dictionary.keys():
    for SUBTYPE in wp_y_rainfed_dictionary[TYPE].keys():
        writer_b.writerow(["CROP",      "RAINFED",    "Yield",            TYPE,SUBTYPE,"nan","nan"])
for TYPE in wp_y_irrigated_dictionary.keys():
    for SUBTYPE in wp_y_irrigated_dictionary[TYPE].keys():
        writer_b.writerow(["CROP",      "IRRIGATED",  "Yield rainfall",   TYPE,SUBTYPE,"nan","nan"])
        writer_b.writerow(["CROP",      "IRRIGATED",  "Incremental yield",TYPE,SUBTYPE,"nan","nan"])
        writer_b.writerow(["CROP",      "IRRIGATED    ","Total yield",    TYPE,SUBTYPE,"nan","nan"])

for TYPE in wp_y_non_crop_dictionary.keys():
    for SUBTYPE in wp_y_non_crop_dictionary[TYPE].keys():
        writer_b.writerow(["NON-CROP",  "RAINFED",    "Yield",            TYPE,SUBTYPE,"nan","nan"])
        writer_b.writerow(["NON-CROP",  "IRRIGATED",  "Yield rainfall",   TYPE,SUBTYPE,"nan","nan"])
        writer_b.writerow(["NON-CROP",  "IRRIGATED",  "Incremental yield",TYPE,SUBTYPE,"nan","nan"])
        writer_b.writerow(["NON-CROP",  "IRRIGATED",  "Total yield",      TYPE,SUBTYPE,"nan","nan"])
```

#### Sheet 4 & Sheet 6

**Sheet 4**

`create_sheet4_6()`

  - _SUPPLY_SURFACEWATER_, `supply_sw_tif`
  - _SUPPLY_GROUNDWATER_, `supply_gw_tif`
  - _CONSUMED_ET_, `conventional_et_tif`
  - _CONSUMED_OTHER_, `other_consumed_tif`
  - _NON_CONVENTIONAL_ET_, `non_conventional_et_tif`
  - _RECOVERABLE_SURFACEWATER_, `recov_sw_tif`
  - _RECOVERABLE_GROUNDWATER_, `recov_gw_tif`
  - _NON_RECOVERABLE_SURFACEWATER_, `non_recov_sw_tif`
  - _NON_RECOVERABLE_GROUNDWATER_, `non_recov_gw_tif`
  - _DEMAND_, `demand_tif`

`create_sheet4_csv()`

```Python
required_landuse_types = ['Wetlands','Greenhouses','Rainfed Crops','Residential','Industry','Natural Grasslands',
                          'Forests','Shrubland','Managed water bodies','Other (Non-Manmade)','Aquaculture',
                          'Power and Energy',
                          'Forest Plantations', 'Irrigated crops','Other','Natural Water Bodies']

first_row = ['LANDUSE_TYPE'] + results.keys()

for flow in results.keys():
    row.append(results[flow][lu_type] * convert_unit)
writer.writerow(row)

```

**Sheet 6**

`create_sheet4_6()`

  - _VERTICAL_RECHARGE_, `recharge_tif`
  - _VERTICAL_GROUNDWATER_WITHDRAWALS_, `supply_gw_tif`
  - _RETURN_FLOW_GROUNDWATER_, `return_flow_gw_gw_tif`
  - _RETURN_FLOW_SURFACEWATER_, `return_flow_sw_gw_tif`

  - _CapillaryRise_, `capillaryrise`
  - _DeltaS_, `'nan'`
  - _ManagedAquiferRecharge_, `'nan'`
  - _Baseflow_, `baseflow`
  - _GWInflow_, `'nan'`
  - _GWOutflow_, `'nan'`

`create_sheet6_csv()`

```Python
required_landuse_types = ['Wetlands','Greenhouses','Rainfed Crops','Residential','Industry','Natural Grasslands',
                          'Forests','Shrubland','Managed water bodies','Other (Non-Manmade)','Aquaculture',
                          'Forest Plantations', 'Irrigated crops','Other','Natural Water Bodies',
                          'Glaciers']

first_row = ['LANDUSE_TYPE'] + results.keys()

for flow in results.keys():
    row.append(results[flow][lu_type] * convert_unit)
writer.writerow(row)
```

#### Sheet 5

`create_csv()`

  - _SUBBASIN_
  - _VARIABLE_
  - _VALUE_
  - _UNITS_

```Python
first_row = ['SUBBASIN', 'VARIABLE', 'VALUE', 'UNITS']

for sb in results['surf_runoff'].keys():
    writer.writerow([sb, 'Inflow',                      '{0}'.format(results['inflows'][sb]),                   'km3'])
    for lu_class in ['PROTECTED', 'UTILIZED', 'MODIFIED', 'MANAGED']:
        writer.writerow([sb, 'Fast Runoff: '+lu_class,  '{0}'.format(results['surf_runoff'][sb][lu_class]),     'km3'])
        writer.writerow([sb, 'Slow Runoff: ' +lu_class, '{0}'.format(results['base_runoff'][sb][lu_class]),     'km3'])
    writer.writerow([sb, 'Total Runoff',                '{0}'.format(results['total_runoff'][sb]),              'km3'])
    writer.writerow([sb, 'SW withdr. manmade',          '{0}'.format(results['withdrawls'][sb]['man']),         'km3'])
    writer.writerow([sb, 'SW withdr. natural',          '{0}'.format(results['withdrawls'][sb]['natural']),     'km3'])
    writer.writerow([sb, 'SW withdr. total',            '{0}'.format(results['withdrawls'][sb]['man']+results['withdrawls'][sb]['natural']), 'km3'])
    writer.writerow([sb, 'Return Flow SW',              '{0}'.format(results['return_sw_sw'][sb]),              'km3'])
    writer.writerow([sb, 'Return Flow GW',              '{0}'.format(results['return_gw_sw'][sb]),              'km3'])
    writer.writerow([sb, 'Total Return Flow',           '{0}'.format(results['return_sw_sw'][sb]+results['return_gw_sw'][sb]), 'km3'])
    writer.writerow([sb, 'Outflow: Total',              '{0}'.format(results['total_outflow'][sb]),             'km3'])
    writer.writerow([sb, 'Outflow: Committed',          '{0}'.format(results['committed_outflow'][sb]),         'km3'])
    writer.writerow([sb, 'Outflow: Non Recoverable',    '{0}'.format(results['non_recoverable_outflow'][sb]),   'km3'])
    writer.writerow([sb, 'Outflow: Non Utilizable',     '{0}'.format(results['non_utilizable_outflow'][sb]),    'km3'])
    writer.writerow([sb, 'Outflow: Utilizable',         '{0}'.format(results['utilizable_outflow'][sb]),        'km3'])
    writer.writerow([sb,'Interbasin Transfer',          '{0}'.format(results['interbasin_transfers'][sb]),      'km3'])
    writer.writerow([sb, 'SW storage change',           '{0}'.format(results['deltaS'][sb]),                    'km3'])
```

#### Sheet 7

`create_csv()`

  - _LAND_USE_
  - _VARIABLE_
  - _SERVICE_
  - _VALUE_
  - _UNITS_

```Python
first_row = ['LAND_USE', 'VARIABLE', 'SERVICE', 'VALUE', 'UNITS']

for lu_class in ['PROTECTED', 'UTILIZED', 'MODIFIED', 'MANAGED']:
    writer.writerow([lu_class, 'Total Runoff',                  'Non-consumptive',          '{0:.3f}'.format(results['tot_runoff'][lu_class]),             'km3'])
    writer.writerow([lu_class, 'Groundwater Recharge',          'Non-consumptive',          '{0:.3f}'.format(results['gw_rech'][lu_class]),                'km3'])
#    writer.writerow(['PROTECTED','Natural water storage in lakes', 'Non-consumptive',      '{0:.2f}'.format(results['nat_stor']),'km3'])
#    writer.writerow(['PROTECTED','Inland Capture Fishery',         'Non-consumptive',      '{0:.2f}'.format(results['fish']),'t'])
    writer.writerow([lu_class, 'Natural Feed Production',       'Incremental ET natural',   '{0:.3f}'.format(results['feed_incremental'][lu_class]),       't'])
    writer.writerow([lu_class, 'Natural Feed Production',       'Landscape ET',             '{0:.3f}'.format(results['feed_landscape'][lu_class]),         't'])
    writer.writerow([lu_class, 'Natural Fuel Wood Production',  'Incremental ET natural',   '{0:.3f}'.format(results['fuel_incremental'][lu_class]),       't'])
        writer.writerow([lu_class, 'Natural Fuel Wood Production',  'Landscape ET',         '{0:.3f}'.format(results['fuel_landscape'][lu_class]),         't'])
    writer.writerow([lu_class, 'Dry Season Baseflow',           'Non-consumptive',          '{0:.3f}'.format(results['baseflow'][lu_class]),               'km3'])
#    writer.writerow(['PROTECTED','Groundwater Recharge',           'SURFACE WATER',        'Flood', 0.])
    writer.writerow([lu_class, 'Root Zone Water Storage',       'Non-consumptive',          '{0:.3f}'.format(results['root_storage'][lu_class]),           'km3'])
    writer.writerow([lu_class, 'Atmospheric Water Recycling',   'Incremental ET natural',   '{0:.3f}'.format(results['atm_recycl_incremental'][lu_class]), 'km3'])
    writer.writerow([lu_class, 'Atmospheric Water Recycling',   'Landscape ET',             '{0:.3f}'.format(results['atm_recycl_landscape'][lu_class]),   'km3'])

```

# [Examples](examples/README.md#data)
