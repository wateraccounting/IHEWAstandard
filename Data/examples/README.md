# IHEWAstandard.Data.examples

Define the **Data examples** of WaterAccounting Tools.


## GTiff

  - [GTiff.Classic.tif](GTiff.Classic.tif)
  - [GTiff.Big.tif](GTiff.Big.tif)


## NetCDF

Nile basin, Precipitation

```Python
netcdf 'p_monthly.nc' {
  dimensions:
    latitude = 36037;
    longitude = 16734;
    time = UNLIMITED;   // (34 currently)
  variables:
    float latitude(latitude=36037);
      :_FillValue = -9999.0f; // float

    float Precipitation(time=34, latitude=36037, longitude=16734);
      :_FillValue = -9999.0f; // float
      :least_significant_digit = 3; // int
      :units = "mm/month";
      :quantity = "Precipitation";
      :source = "WaPOR";
      :period = "month";
      :_ChunkSizes = 1U, 1502U, 670U; // uint

    float longitude(longitude=16734);
      :_FillValue = -9999.0f; // float

    float time(time=34);
      :_FillValue = -9999.0f; // float
      :calendar = "standard";
      :units = "days since 1970-01-01 00:00";
      :_ChunkSizes = 1024U; // uint

  // global attributes:
  :basin_name = "Nile";
}
```

## SVG

