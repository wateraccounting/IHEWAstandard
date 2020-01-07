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

Base configuration Yaml file, contains _`messages:`_ and _`products:`_.

_`products:`_ has the structure, _product_ -> _version_ -> _parameter_ -> _resolution_ -> _variable_.

  - _product_: All upper characters, ex. ALEXI.
  - _version_: Start with 'v', ex. v1, v2.0.
  - _parameter_: Use IHEWAstandard.Engine.Data.Long Name, ex. SoilWaterIndex.
  - _resolution_: Following talbes, **Resolution types**, Temporal, Spatial Resolution.
  - _variable_: Use IHEWAstandard.Engine.Data, and special variable cases, ex. **ASCAT**.soil_water_index.SWI_010, **CFSR**.Radiation.dlwsfc, **DEM**.DEM.af 

File

| Name         | Description                                           | Location     |
| -----------: |------------------------------------------------------ | ------------ |
| _`fname:r:`_ | remote file to be downloaded, should delete           | ./remote/    |
| _`fname:t:`_ | temporary file to be generated, should delete         | ./temporary/ |
| _`fname:l:`_ | WaterAccounting file to be saved, should keep         | ./download/  |

File Name Template

 _`freq:`_ = `null`:
> ./download/ _parameter_ / _resolution_ / _variable_ / _product_ \_ _version_ \_ _`units:l:`_ .tif

 _`freq:`_ = [yearly]:
> ./download/ _parameter_ / _resolution_ / _variable_ / _product_ \_ _version_ \_ _`units:l:`_ \_ _`freq:`_ - `%Y` .tif

 _`freq:`_ = [monthly]:
> ./download/ _parameter_ / _resolution_ / _variable_ / _product_ \_ _version_ \_ _`units:l:`_ \_ _`freq:`_ - `%Y` `%m` .tif

 _`freq:`_ = [daily, weekly, dekadal]:
> ./download/ _parameter_ / _resolution_ / _variable_ / _product_ \_ _version_ \_ _`units:l:`_ \_ _`freq:`_ - `%Y` `%m` `%d` .tif

 _`freq:`_ = [hourly]:
> ./download/ _parameter_ / _resolution_ / _variable_ / _product_ \_ _version_ \_ _`units:l:`_ \_ _`freq:`_ - `%Y` `%m` `%d` \_ `%H` `%M` .tif

**None value**

YAML value `null` applyed to: 

  - _product_
    - _`account:`_
    - _version_
      - _parameter_
        - _resolution_
          - _`freq:`_
          - _`variables:`_
            - _variable_
              - _`dfmt:`_
              - _`rfmt:`_
              - _`tfmt:`_
              - _`fname:`_
              - _`ftype:`_
              - _`dtype:`_
              - _`time:`_

**File Name Alias**

| Name/Code  | Description                               | Format                 | Example                            |
| ---------: |------------------------------------------ | ---------------------- | ---------------------------------- |
| **Variable Name**                                                                                                    |
| ~~var~~    | Variable name, lower case                 | `{var:s}`              |                                    |
| ~~Var~~    | Variable name, upper case                 | `{Var:s}`              |                                    |
| **File Part**, `ipart`                                                                                               |
| `i`        | ith part of file, `for i in range(4)`     | `{i:d}`                | 1, CFSR                            |
| **Lat Lon**,   `latlon`                                                                                              |
| ~~latlon~~ | DEM tile's name                           | `{lat:>03s}{lon:>04s}` | 'n00e005'                          |
| `lat`      | DEM tile's name, Lat                      | `{lat:>03s}`           | 'n00'  's01',   DEM / '80N',  JRC  |
| `lon`      | DEM tile's name, Lon                      | `{lon:>04s}`           | 'e001' 'w001' , DEM / '180W', JRC  |
| **Datetime**,  `dtime` [link](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes)    |
| `%Y`       | Year                                      | `{Y:>04s}`             | '2019'                             |
| `%y`       | Year                                      | `{Y:>02s}`             | '19', FEWS                         |
| `%m`       | Month                                     | `{M:>02s}`             | '01'                               |
| `%d`       | Day of month                              | `{D:>02s}`             | '01'                               |
| `%j`       | Day of year                               | `{d:>03s}`             | '365'                              |
| `%H`       | Hour                                      | `{h:>02s}`             | '24'                               |
| `%M`       | Minute                                    | `{m:>02s}`             | '01'                               |
| `%S`       | Second                                    | `{s:>02s}`             | '01'                               |
| `%f`       | Millisecond                               | `{ms:>02s}`            | ''                                 |
| **Units**                                                                                                            |
| '.'        | Dimensionless, Index, Percent             |                        |                                    |
| 'mm'       | Millimetre                                |                        |                                    |
| 'mm.d'     | Millimetre per day                        |                        |                                    |
| 'MJ.m2.d'  | Mega Joule per m2 per day                 |                        |                                    |
| 'W.m2'     | Watt per m2                               |                        |                                    |
| 'kg.m2.s'  | Kilogram per m2 per second                |                        | 86400 * mm.d                       |

example

```Python
import datetime
print('{dtime:%Y-%m-%d %H:%M}'.format(dtime=datetime.datetime(2001, 2, 3, 4, 5)))

"2001-02-03 04:05"
```

**File types**

`Driver.FileExtension`

File driver

| Name/Code    | Ext               | File type        | GDAL Drivers                                                        |
| -----------: | ----------------- | ---------------- | ------------------------------------------------------------------- |
| GRIB         | .grb2             | Raster file      | [GRIB](https://gdal.org/drivers/raster/grib.html#raster-grib)       |
| GRIB         | .grib2            | Raster file      | [GRIB](https://gdal.org/drivers/raster/grib.html#raster-grib)       |
| GTiff        | .tif              | Raster file      | [GTiff](https://gdal.org/drivers/raster/gtiff.html#raster-gtiff)    |
| NetCDF       | .nc               | NetCDF file      | [netCDF](https://gdal.org/drivers/raster/netcdf.html#raster-netcdf) |
| NetCDF       | .nc4              | NetCDF file      | [netCDF](https://gdal.org/drivers/raster/netcdf.html#raster-netcdf) |
| NetCDF.Group | .HDF5, .HDF       | NetCDF file      | [netCDF](https://gdal.org/drivers/raster/netcdf.html#raster-netcdf) |
| HDF5         | .HDF5             | HDF5 file        | [HDF5](https://gdal.org/drivers/raster/hdf5.html#raster-hdf5)       |
| HDF4         | .HDF              | HDF4 file        | [HDF4](https://gdal.org/drivers/raster/hdf4.html#raster-hdf4)       |
| AIG          | .adf              | Raster file      | [AIG](https://gdal.org/drivers/raster/aig.html#raster-aig)          |
| EHdr         | .bil              | Raster file      | [EHdr](https://gdal.org/drivers/raster/ehdr.html#raster-ehdr)       |
| EHdr         | .hdr              | Header file      | [EHdr](https://gdal.org/drivers/raster/ehdr.html#raster-ehdr)       |
| EHdr         | .blw              | World file       | [EHdr](https://gdal.org/drivers/raster/ehdr.html#raster-ehdr)       |
| EHdr         | .stx              | Statistics file  | [EHdr](https://gdal.org/drivers/raster/ehdr.html#raster-ehdr)       |
| **Other**                                                                                                                 |
| gz           | .gz -> dat(`<f4`) | Binary file      |                                                                     |
| zip          | .zip              | Binary file      |                                                                     |
| MEM          | Memory            | Raster file      | [MEM](https://gdal.org/drivers/raster/mem.html#raster-mem)          |
| DODS         | DODS/OPeNDAP      | Vector file      | [DODS](https://gdal.org/drivers/vector/dods.html#vector-dods)       |

**Resolution types**

 - Minute and second, [Arc](https://en.wikipedia.org/wiki/Minute_and_second_of_arc)
 - Spatial Resolution, [LatLon](https://calgary.rasc.ca/latlong.htm)
 - Temporal Resolution, [watools.Functions.Start.Download_Data.Set_Start_End_Dates()](https://github.com/wateraccounting/watools/blob/master/Functions/Start/Download_Data.py#L771)
    - [strftime codes](http://strftime.org/)
    - [datetime format codes](https://docs.python.org/3.7/library/datetime.html#strftime-and-strptime-behavior)
    - [pandas DateOffset](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#dateoffset-objects)
    - [pandas date_range alias](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#timeseries-offset-aliases)

_resolution_ [**Spatial**, 'Name/Code']

| Name/Code  | sec/min        | degree   	         | meters/km                      |
| ---------: |--------------- | ------------------ | ------------------------------ |
| 0.1s       | 0.1 arc-second | 0.0000277777777777 | approx. 3 m     at the equator |
| 1s         | 1 arc-second   | 0.0002777777777777 | approx. 30 m    at the equator |
| 3s         | 3 arc-second   | 0.0008333333333333 | approx. 90 m    at the equator |
| 15s        | 15 arc-second  | 0.0041666666666667 | approx. 500 m   at the equator |
| 30s        | 30 arc-second  | 0.0083333333333333 | approx. 1 km    at the equator |
| 1m         | 1 arc-minute   | 0.0166666666666666 | approx. 2 km    at the equator |
| 5m         | 5 arc-minute   | 0.0833333333333333 | approx. 10 km   at the equator |
| 6m         | 6 arc-minute   | 0.1                | approx. 12 km   at the equator |
| 15m        | 15 arc-minute  | 0.2499999999999999 | approx. 30 km   at the equator |

_resolution_ [**Temporal**, 'Standard Name']

_`freq:`_ [**Temporal**, 'Name/Code']

| Name/Code  | Standard Name  | Long Name      | datetime | pandas   | Description   |
| ---------: | -------------- | -------------- | -------- | -------- | ------------- |
| `null`     |                |                |          |          |               |
| H          | hourly         | Hourly         | %H       | H        |               |
| 3H         | three_hourly   | Three Hourly   |          | 3H       |               |
| 6H         | six_hourly     | Six Hourly     |          | 6H       |               |
| D          | daily          | Daily          | %d       | D        |               |
| 7D         | weekly         | Weekly         | %W / %U  | 7D       |               |
| 8D         | eight_daily    | Eight Daily    |          | 8D       |               |
| 10D        | dekadal        | Dekadal        |          | 10D      |               |
| 16D        | sixteen_daily  | Sixteen Daily  |          | 16D      |               |
| MS         | monthly        | Monthly        | %m       | MS       | Monthly Start |
| M          | monthly        | Monthly        | %m       | M        | Monthly End   |
| AS         | yearly         | Yearly         | %Y       | AS       | Yearly Start  |
| Y          | yearly         | Yearly         | %Y       | Y        | Yearly End    |

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

**Protocal types**

| Protocals  | Python Dependency           | auth | get | post | crawl | example |
| ---------: |---------------------------- | ---- | --- | ---- | ----- | ------- |
| FTP        | ftplib                      | Y    | Y   |      |       |         |
| SFTP       | paramiko                    | Y    | Y   |      |       |         |
| HTTP/HTTPS | requests                    | Y    | Y   |      |       |         |
| HTTP/HTTPS | urllib                      | H    | Y   |      |       |         |
| HTTP/HTTPS | pycurl                      |      | Y   |      |       |         |
| HTTP/HTTPS | BeautifulSoup               |      |     |      | Y     | MCD43   |
| TDS        | pytds (python-tds)          |      | Y   |      |       |         |
| API        | ecmwfapi (ecmwf-api-client) | Y    |     |      |       | ECMWF   |

_product_ -> _version_ -> _parameter_ -> _resolution_ -> _variable_.method
  - get:  download, with single url
  - auth: download, with single url and header
  - post: download, with _product_._`account:`_ is not `null` and data

  - crawl: scan resources
  - Y: Yes
  - H: Header, bas64encode

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
      resolutions:                                                                  #   temporal/spacial resolution
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
              variable: null                                                        #   variable name in the NetCDF
              name: 'Daily Evapotranspiration'                                      #   long name 
              description:                                                          #   description
                ''                                                                  # 
              dfmt: null                                                            #   remote dir format
              rfmt: 'dtime'                                                         #   remote file format
              tfmt: 'dtime'                                                         #   temporary file format
              dir: '/WaterAccounting/Data_Satellite/Evaporation/ALEXI/'             #   data location on the data potal/repository
              fname:                                                                #   file name
                r: 'EDAY_CERES_{dtime:%Y%j}.dat.gz'                                 #     remote file,            string, template
                t: 'EDAY_CERES_{dtime:%Y%j}.dat'                                    #     temporary file,         string, template
                l: 'ALEXI_v1_mm.d_D-{dtime:%Y%m%d}.tif'                             #     local/downloaded file,  string, template
              ftype:                                                                #   file type/extension
                r: 'gz'                                                             #     remote file,            string
                t: 'dat'                                                            #     temporary file,         string
                l: 'GTiff'                                                          #     local/downloaded file,  string
              dtype:                                                                #   data type
                r: 'binary'                                                         #     remote file,            string, numpy style
                t: 'float32'                                                        #     temporary file,         string, numpy style
                l: 'float32'                                                        #     local/downloaded file,  string, numpy style
              units:                                                                #   data unit
                r: 'MJ.m2.d'                                                        #     remote file,            string
                l: 'mm.d'                                                           #     local/downloaded file,  string
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
                e: 2016-12-31                                                       #     end,                    string, 'yyyy-mm-dd'
              dem:                                                                  #   demension
                w: -9999                                                            #     width,                  integer
                h: -9999                                                            #     height,                 integer
```

## Resources

[Products](https://ihewacollect.readthedocs.io/en/latest/)

[NASA, OPeNDAP and GDS](https://disc.gsfc.nasa.gov/information/tools?title=OPeNDAP%20and%20GDS)

# [Examples](examples/README.md#ihewacollect)
