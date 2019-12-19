# IHEWAstandard.Configuration.IHEWAcollect

Define the **Configuration.IHEWAcollect standard** of WaterAccounting Tools.

**TOC**

  - [Standard](#standard)
    - [accounts.yaml](#accountsyaml)
    - [base.yaml](#baseyaml)
  - [Resources](#resources)
  - [Examples](#examples)


## Standard

### accounts.yaml

Accounts configuration Yaml file, contains

_Template_

```Yaml
accounts:
  FTP_WA_GUESS:
    username: 'wateraccountingguest'
    password: 'W@t3r@ccounting'
    apitoken: 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
```

### base.yaml

Base configuration Yaml file, contains `messages` and `products`.

`products` has the structure, _product_ -> _version_ -> _parameter_ -> _resolution_ -> _variable_.

  - _product_: All upper characters, ex. ALEXI.
  - _version_: Start with 'v', ex. v1, v2.0.
  - _parameter_: Use IHEWAstandard.Engine.Data.Long Name, ex. SoilWaterIndex.
  - _resolution_: Following talbes, **Resolution types**, Temporal, Spatial Resolution.
  - _variable_: Use IHEWAstandard.Engine.Data, and special variable cases, ex. **ASCAT**.soil_water_index.SWI_010, **CFSR**.Radiation.dlwsfc, **DEM**.DEM.af 

**None value**

YAML value `null` applyed to: 

  - _roduct_
    - `account:`
    - _version_
      - _parameter_
        - _resolution_
          - `freq:`
          - `variables:`
            - _variable_
              - `fname:`
              - `ftype:`
              - `dtype:`
              - `unit:`
              - `time:`

**Name**

| Name       | Description                               | Format              | Example   |
| ---------: |------------------------------------------ | ------------------- | --------- |
| ~~var~~    | variable name, lower case                 | `{var:s}`           |           |
| ~~Var~~    | variable name, upper case                 | `{Var:s}`           |           |
| i          | ith part of file, `for i in range(4)`     | `{i:d}`             | 1         |
| Y          | year                                      | `{Y:>04s}`          | '2019'    |
| M          | month                                     | `{M:>02s}`          | '01'      |
| D          | day of month                              | `{D:>02s}`          | '01'      |
| d          | day of year                               | `{d:>03s}`          | '365'     |
| h          | hour                                      | `{h:>02s}`          | '24'      |
| m          | minute                                    | `{m:>02s}`          | '01'      |
| s          | second                                    | `{s:>02s}`          | '01'      |
| ms         | millisecond                               | `{ms:>02s}`         | ''        |
| ~~latlon~~ | DEM tile's name                           | `{n:>03s}{e:>03s}`  | 'n00e005' |

example

```Python
import datetime
print('{ymd:%Y-%m-%d %H:%M}'.format(ymd=datetime.datetime(2001, 2, 3, 4, 5)))

"2001-02-03 04:05"
```

**Resolution types**

Temporal Resolution, [watools.Functions.Start.Download_Data.Set_Start_End_Dates()](https://github.com/wateraccounting/watools/blob/master/Functions/Start/Download_Data.py#L771)

  * [strftime codes](http://strftime.org/)
  * [datetime format codes](https://docs.python.org/3.7/library/datetime.html#strftime-and-strptime-behavior)
  * [pandas DateOffset](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#dateoffset-objects)
  * [pandas date_range alias](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#timeseries-offset-aliases)

| Name           | datetime | pandas   |
| -------------: | -------- | -------- |
| hourly         | %H       | H        |
| three_hourly   |          | 3H       |
| six_hourly     |          | 6H       |
| daily          | %d       | D        |
| weekly         | %W / %U  | 7D       |
| eight_daily    |          | 8D       |
| dekadal        |          | 10D      |
| sixteen_daily  |          | 16D      |
| monthly, start | %m       | MS       |
| monthly, end   | %m       | M        |
| yearly, start  | %Y       | AS       |
| yearly, end    | %Y       | Y        |

_Template_

```Python
if freq == 'MS':
    files = glob.glob('*monthly_%d.%02d.01.tif' % (year, month))
if freq == 'AS':
    files = glob.glob('*yearly_%d.%02d.01.tif' % (year, month))
if freq == 'D':
    files = glob.glob('*daily_%d.%02d.%02d.tif' % (year, month, day))
if freq == '8D':
    files = glob.glob('*8-daily_%d.%02d.%02d.tif' % (year, month, day))
if freq == '16D':
    files = glob.glob('*16-daily_%d.%02d.%02d.tif' % (year, month, day))
```

Spatial Resolution
  
  * [LatLon](https://calgary.rasc.ca/latlong.htm)

| Name       | sec/min        | degree   	         | meters/km                      |
| ---------: |--------------- | ------------------ | ------------------------------ |
| 0.1s       | 0.1 arc-second | 0.0000277777777777 | approx. 3 m     at the equator |
| 1s         | 1 arc-second   | 0.0002777777777777 | approx. 30 m    at the equator |
| 3s         | 3 arc-second   | 0.0008333333333333 | approx. 90 m    at the equator |
| 15s        | 15 arc-second  | 0.0041666666666667 | approx. 500 m   at the equator |
| 30s        | 30 arc-second  | 0.0083333333333333 | approx. 1 km    at the equator |
| 1m         | 1 minute       | 0.0277777777777777 | approx. 2 km    at the equator |
| 5m         | 5 minute       | 0.0833333333333333 | approx. 10 km   at the equator |
| 6m         | 6 minute       | 0.1                | approx. 12.5 km at the equator |
| 15m        | 15 minute      | 0.2499999999999999 | approx. 30 km   at the equator |

**Protocal types**

| Protocals  | Python Dependency           | get | post | api |
| ---------: |---------------------------- | --- | ---- | --- |
| FTP        | from ftplib import FTP      | Y   |      |     |
| HTTP/HTTPS | import requests (requests)  | Y   |      |     |
| HTTP/HTTPS | urllib.request (urllib)     | Y   |      |     |
| HTTP/HTTPS | pycurl.Curl (pycurl)        | Y   |      |     |
| TDS        | pytds (python-tds)          | Y   |      |     |
| ECMWF      | ecmwfapi (ecmwf-api-client) |     |      | Y   |

**File types**

`Driver.FileExtension`

File name

| Name       | Description                                           |
| ---------: |------------------------------------------------------ |
| rmtfile    | remote file downloaded to `./remote/`, to delete      |
| tmpfile    | temporary file generated to `./temporary/`, te delete |
| locfile    | WaterAccounting file saved to `./download/`, to keep  |

File driver

| Name      | Ext               | File type        | GDAL Drivers                                                        |
|           | ----------------: | ---------------- | ------------------------------------------------------------------- |
| GRIB      | .grb2             | Raster file      | [GRIB](https://gdal.org/drivers/raster/grib.html#raster-grib)       |
| GRIB      | .grib2            | Raster file      | [GRIB](https://gdal.org/drivers/raster/grib.html#raster-grib)       |
| GTiff     | .tif              | Raster file      | [GTiff](https://gdal.org/drivers/raster/gtiff.html#raster-gtiff)    |
| NetCDF    | .nc               | NetCDF file      | [netCDF](https://gdal.org/drivers/raster/netcdf.html#raster-netcdf) |
| AIG       | .adf              | Raster file      | [AIG](https://gdal.org/drivers/raster/aig.html#raster-aig)          |
| EHdr      | .bil              | Raster file      | [EHdr](https://gdal.org/drivers/raster/ehdr.html#raster-ehdr)       |
| EHdr      | .hdr              | Header file      | [EHdr](https://gdal.org/drivers/raster/ehdr.html#raster-ehdr)       |
| EHdr      | .blw              | World file       | [EHdr](https://gdal.org/drivers/raster/ehdr.html#raster-ehdr)       |
| EHdr      | .stx              | Statistics file  | [EHdr](https://gdal.org/drivers/raster/ehdr.html#raster-ehdr)       |
| **Other**                                                                                                              |
| gz        | .gz -> dat(`<f4`) | Binary file      |                                                                     |
| zip       | .zip              | Binary file      |                                                                     |
| MEM       | Memory            | Raster file      | [MEM](https://gdal.org/drivers/raster/mem.html#raster-mem)          |
| DODS      | DODS/OPeNDAP      | Vector file      | [DODS](https://gdal.org/drivers/vector/dods.html#vector-dods)       |

_Template_

```Yaml
products:
  ALEXI:                                                                            # `product`
    account: 'FTP_WA'                                                               # accounts.yml
    meta:                                                                           # product metadata
      owner: 'IHE Delft'                                                            #   product owner/developer/maintainer...
      description:                                                                  #   description
        'Product description'                                                       #   
      websites:                                                                     #   official websites
        - 'https://www.wateraccounting.org'
      protocols:                                                                    #   web protocols, ex. HTTP/HTTPS...
        - 'FTP'
      methods:                                                                      #   dependency (python) used to download 
        - 'ftp'
      ftypes:                                                                       #   hosted file types
        - 'gz'
        - 'GTiff'
      versions:                                                                     #   version list
        - 'v1'
      datasets:                                                                     #   datasets
        - 'Evapotranspiration'
      datatypes:                                                                    #   temporal/spacial resolution
        - 'daily'
        - 'weekly'
      projection:                                                                   #   EPSG Geodetic Parameter Dataset of Coordinate Reference Systems (crs)
        - 'EPSG:4326 - WGS 84 - Geographic'
    v1:                                                                             # `product.version`
      evapotranspiration:                                                                  # `product.version.parameter`
        daily:                                                                      # `product.version.parameter.resolution`
          url: 'ftp://ftp.wateraccounting.unesco-ihe.org'                           #   data potal/repository url
          method: 'get'                                                             #   request methods [get, post, ...]
          freq: 'D'                                                                 #   `resolution` short name, follow pandas.datetime
          variables:                                                                #
            ETA:                                                                    # `product.version.parameter.resolution.variable`
              name: 'Daily Evaporation'                                             #   long name 
              description:                                                          #   description
                ''                                                                  # 
              dir: '/WaterAccounting/Data_Satellite/Evaporation/ALEXI/'             #   data location on the data potal/repository
              fname:                                                                #   file name
                r: 'EDAY_CERES_{Y:>04s}{d:>03s}.dat.gz'                             #     remote file,            string, template
                t: 'EDAY_CERES_{Y:>04s}{d:>03s}.dat'                                #     temporary file,         string, template
                l: 'ALEXI_v1_mmpd_daily-{Y:>04s}_{M:>02s}_{D:>02s}.tif'             #     local/downloaded file,  string, template
              ftype:                                                                #   file type/extension
                r: 'gz'                                                             #     remote file,            string
                t: 'dat'                                                            #     temporary file,         string
                l: 'GTiff'                                                          #     local/downloaded file,  string
              dtype:                                                                #   data type
                r: 'binary'                                                         #     remote file,            string, numpy style
                t: 'float32'                                                        #     temporary file,         string, numpy style
                l: 'float32'                                                        #     local/downloaded file,  string, numpy style
              unit:                                                                 #   data unit
                r: 'MJ/m2d'                                                         #     remote file,            string
                l: 'mm/d'                                                           #     local/downloaded file,  string
                m: 2.45                                                             #     multiplyer,             float
              lat:                                                                  #   latitude
                s: -60.0                                                            #     south,                  float
                n: 70.0                                                             #     north,                  float
                r: 0.05                                                             #     resolution,             float
              lon:                                                                  #   longitude
                w: -180.0                                                           #     west,                   float
                e: 180.0                                                            #     east,                   float
                r: 0.05                                                             #     resolution,             float
              time:                                                                 #   time
                s: 2005-01-01                                                       #     start,                  string, 'yyyy-mm-dd'
                e: null                                                             #     end,                    string, 'yyyy-mm-dd'
              dem:                                                                  #   demension
                w: -9999                                                            #     width,                  integer
                h: -9999                                                            #     height,                 integer
```

## Resources

[Products](https://ihewacollect.readthedocs.io/en/latest/)

[NASA, OPeNDAP and GDS](https://disc.gsfc.nasa.gov/information/tools?title=OPeNDAP%20and%20GDS)

# [Examples](examples/README.md#ihewacollect)
