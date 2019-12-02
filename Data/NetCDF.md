# IHEWAstandard.Data.NetCDF

Define the **Data.NetCDF standard** of WaterAccounting Tools.

[OGC Standard, NetCDF](https://www.opengeospatial.org/standards/netcdf)
[NetCDF Code](https://github.com/Unidata/netcdf4-python)

[NetCDF Best Practices](https://www.unidata.ucar.edu/software/netcdf/docs/BestPractices.html)


## WaterPix


### Input

#### Dimensions

#### Variables of Dimension

#### Variables of Data

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


### Output

#### Dimensions

  - `lat_dim` = out_nc.createDimension(**inp_lat.standard_name**, `lat_n`)
  - `lon_dim` = out_nc.createDimension(**inp_lon.standard_name**, `lon_n`)
  - `time_dim` = out_nc.createDimension('**time_yyyymm**', `time_n`)
  - `year_dim` = out_nc.createDimension('**time_yyyy**', `years_n`)

#### Variables of Dimension

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

#### Variables of Data 

Monthly: **('time_yyyymm', 'latitude', 'longitude')**

Yearly: **('time_yyyy', 'latitude', 'longitude')**

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


## Hyperloop


### Input


  - `basins`, Define basin specific parameters
  - `global_data`, Define output folder and WaterPix file
  - `data`, Define paths of folders with temporal tif files

#### basins, {`ID`: metadata}

```Python
data = {
  'ID': {
    'name': '',
    'lu': '',
    'full_basin_mask': '',
    'masks': '',
    'crops': '',
    'non_crop': '',
    'recycling_ratio': '',
    'dico_in': '',
    'dico_out': '',
    'GRACE': '',
    'fractioin_xs': '',
    'discharge_out_from_wp': '',
    'lu_based_supply_split': '',
    'grace_supply_split': '',
    'grace_split_alpha_bounds': '',
    'water_year_start_month': '',
    'ndm_max_original': ''
  }
}
```

#### global_data, {`variable_name`: path}

```Python
data = {
  'equiped_sw_irrigation': 'Landuse',
  'wpl': 'Gray Water Footprint',
  'environ_water_req': 'EF',
  'population': 'World population',
  'dem': 'HydroSHED.DEM',
  'dir': 'HydroSHED.DIR',
  'waterpix': 'WaterPix'
}
```

#### data, {`folder_name`, path}

```Python
data = {
  'ndm': 'National Drought Model',
  'p': 'Precipitation',
  'et': 'Evapotranspiration',
  'n': 'Rainy Days',
  'lai': 'Leaf Area Index',
  'etref': 'Reference Evapotranspiration',
  'bf': 'Baseflow',
  'sr': 'Surface Runoff',
  'tr': 'Total Runoff',
  'perc': 'Percolation',
  'dperc': 'Incremental Percolation',
  'supply_total': 'Supply',
  'dro': 'Incremental Runoff',
  'etb': 'Blue Evapotranspiration',
  'etg': 'Green Evapotranspiration'
}
```
s

### Output


# [examples](examples/README.md)
