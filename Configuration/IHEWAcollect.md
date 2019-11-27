# IHEWAstandard.Configuration.IHEWAcollect.yml

Define the **Configuration.IHEWAcollect.yml standard** of WaterAccounting Tools.

## base

## None value

`null`: 

  * account
  * data
    * ftype
    * freq
    * unit
    * time

### Data types

#### Temporal Resolution

| Short   | Lone       | Other  |
| ------: |----------- | ------ |
|         | six_hourly |        |
| D       | daily      |        |
| 7D      | weekly     |        |
| 10D     | dekadal    |        |
| MD      | monthly    |        |
|         | pentadal   |        |
| Y       | yearly     |        |

#### Spatial Resolution

| Identifier | sec/min        | degree   	       | meters/km                    |
| ---------: |--------------- | ------------------ | ---------------------------- |
| 3s         | 3 arc-second   | 0.0008333333333333 | approx. 90 m at the equator  |
| 15s        | 15 arc-second  | 0.0041666666666667 | approx. 500 m at the equator |
| 30s        | 30 arc-second  | 0.0083333333333333 | approx. 1 km at the equator  |
| 5m         | 5 minute       | 0.0833333333333333 | approx. 10 km at the equator |

### Protocal

| Protocal   | Python Dependency           |
| ---------: |---------------------------- |
| FTP        | from ftplib import FTP      |
| HTTP/HTTPS | import requests (requests)  |
| HTTP/HTTPS | urllib.request (urllib)     |
| HTTP/HTTPS | pycurl.Curl (pycurl)        |
| TDS        | pytds (python-tds)          |
| ECMWF      | ecmwfapi (ecmwf-api-client) |

### File types, `Driver.FileExtension`

| Ext              | File type        | GDAL Drivers     |
| ---------------: | ---------------- | ---------------- |
| grb2             |                  | [GRIB](https://gdal.org/drivers/raster/grib.html#raster-grib) |
| grib2            |                  | [GRIB](https://gdal.org/drivers/raster/grib.html#raster-grib) |
| tif              |                  | [GTiff](https://gdal.org/drivers/raster/gtiff.html#raster-gtiff) |
| nc               |                  | [netCDF](https://gdal.org/drivers/raster/netcdf.html#raster-netcdf) |
| gz -> dat(`<f4`) |                  |                  |
| adf              |                  | [AIG](https://gdal.org/drivers/raster/aig.html#raster-aig) |
| bil              | Raster data file | [EHdr](https://gdal.org/drivers/raster/ehdr.html#raster-ehdr) |
| hdr              | Header file      |                  |
| blw              | World file       |                  |
| stx              | Statistics file  |                  |


## [examples](examples/README.md)
