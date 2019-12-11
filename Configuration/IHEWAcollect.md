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

```Yaml
accounts:
  FTP_WA_GUESS:
    username: 'wateraccountingguest'
    password: 'W@t3r@ccounting'
    apitoken: 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
```


## base.yaml

Base configuration Yaml file, contains `messages` and `products`.

#### None value

YAML string '`null`' applyed to: 

  * `account`
  * data
    * `ftype`
    * `freq`
    * `unit`
    * `time`


#### Name

| Name       | Description                               |
| ---------: |------------------------------------------ |
| var        | variable name, lower case                 |
| Var        | variable name, upper case                 |
| i          | ith part of file, `for i in range(0, 4):` |
| Y          | year, `stirng[4]`                         |
| m          | month, `stirng[2]`                        |
| d          | day, `stirng[2]`                          |
| j          | day of year, `stirng[3]`                  |
| latlon     | DEM tile's name, `string[7]`, _n00e005_   |

example

```Python
import datetime
print('{ymd:%Y-%m-%d %H:%M}'.format(ymd=datetime.datetime(2001, 2, 3, 4, 5)))

"2001-02-03 04:05"
```


#### Resolution types

##### Temporal Resolution

  * [strftime codes](http://strftime.org/)
  * [datetime format codes](https://docs.python.org/3.7/library/datetime.html#strftime-and-strptime-behavior)
  * [pandas DateOffset](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#dateoffset-objects)
  * [pandas date_range alias](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#timeseries-offset-aliases)

| Name        | datetime | pandas   |
| ----------: | -------- | -------- |
| hourly      | %H       | H        |
| six_hourly  |          | 6H       |
| daily       | %d       | D        |
| weekly      | %W / %U  | 7D       |
| dekadal     |          | 10D      |
| monthly     | %m       | MD       |
| yearly      | %Y       | Y        |

##### Spatial Resolution
  
  * [LatLon](https://calgary.rasc.ca/latlong.htm)

| Name       | sec/min        | degree   	         | meters/km                    |
| ---------: |--------------- | ------------------ | ---------------------------- |
| 0.1s       | 0.1 arc-second | 0.0000277777777777 | approx. 3 m at the equator   |
| 1s         | 1 arc-second   | 0.0002777777777777 | approx. 30 m at the equator  |
| 3s         | 3 arc-second   | 0.0008333333333333 | approx. 90 m at the equator  |
| 15s        | 15 arc-second  | 0.0041666666666667 | approx. 500 m at the equator |
| 30s        | 30 arc-second  | 0.0083333333333333 | approx. 1 km at the equator  |
| 1m         | 1 minute       | 0.0277777777777777 | approx. 2 km at the equator  |
| 5m         | 5 minute       | 0.0833333333333333 | approx. 10 km at the equator |


#### Protocal types

| Protocal   | Python Dependency           |
| ---------: |---------------------------- |
| FTP        | from ftplib import FTP      |
| HTTP/HTTPS | import requests (requests)  |
| HTTP/HTTPS | urllib.request (urllib)     |
| HTTP/HTTPS | pycurl.Curl (pycurl)        |
| TDS        | pytds (python-tds)          |
| ECMWF      | ecmwfapi (ecmwf-api-client) |


#### File types

`Driver.FileExtension`

##### File name

| Name       | Description                                           |
| ---------: |------------------------------------------------------ |
| rmtfile    | downloaded to `./remote/`                             |
| tmpfile    | generated to `./temporary/`, to be deleted at the end |
| locfile    | saved to `./download/`                                |

##### File driver

| Ext               | File type        | GDAL Drivers                                                        |
| ----------------: | ---------------- | ------------------------------------------------------------------- |
| .grb2             | Raster file      | [GRIB](https://gdal.org/drivers/raster/grib.html#raster-grib)       |
| .grib2            | Raster file      | [GRIB](https://gdal.org/drivers/raster/grib.html#raster-grib)       |
| .tif              | Raster file      | [GTiff](https://gdal.org/drivers/raster/gtiff.html#raster-gtiff)    |
| .nc               | NetCDF file      | [netCDF](https://gdal.org/drivers/raster/netcdf.html#raster-netcdf) |
| .gz -> dat(`<f4`) | Binary file      |                                                                     |
| .adf              | Raster file      | [AIG](https://gdal.org/drivers/raster/aig.html#raster-aig)          |
| .bil              | Raster file      | [EHdr](https://gdal.org/drivers/raster/ehdr.html#raster-ehdr)       |
| .hdr              | Header file      | [EHdr](https://gdal.org/drivers/raster/ehdr.html#raster-ehdr)       |
| .blw              | World file       | [EHdr](https://gdal.org/drivers/raster/ehdr.html#raster-ehdr)       |
| .stx              | Statistics file  | [EHdr](https://gdal.org/drivers/raster/ehdr.html#raster-ehdr)       |


## Resources

### Products

| Product       | Version  | Parameter         | resolution        | resolution       | variable  |
| ------------: | -------- | ----------------- | ----------------- |----------------- | --------- |
| ALEXI         | v1       | Evaporation       | resolution        | daily            | ETa       |
| _ECMWF_       |          |                   |                   |                  |           |


# [Examples](examples/README.md#ihewacollect)
