import os

import numpy as np
import pandas as pd

try:
    from osgeo import gdal, osr, gdalconst
except ImportError:
    import gdal
    import osr
    import gdalconst
print(os.environ["GDAL_DATA"])
print(os.environ["GDAL_DRIVER_PATH"])

# print(os.getcwd())
# print(os.path.dirname(os.path.abspath(__file__)))
fpath = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(fpath, '../', 'Data', 'examples', 'GTiff.Classic.tif')

# GTiff array,  [North, West] to [South, East]
# GTiff Origin, [West, North]
# GTiff Extent, [West, South] to [East, North] 
#               pixelWidth   = 10
#               pixelHeight  = -10
band            = 1
originX         = 0.0
originY         = 20.0
rasterWidth     = 2
rasterHeight    = 3
pixelWidth      = 10
pixelHeight     = -10
array           = np.array(
                      [
                          [1, 2],
                          [3, 4],
                          [5, 6]
                      ],
                      dtype=np.float32
                  )
driver = gdal.GetDriverByName('GTiff')

outRaster = driver.Create(
                file,
                xsize=rasterWidth,
                ysize=rasterHeight,
                bands=1,
                eType=gdal.GDT_Float32)

outRaster.SetGeoTransform((originX, pixelWidth, 0, originY, 0, pixelHeight))
outband = outRaster.GetRasterBand(band)
outband.WriteArray(array)

outRasterSRS = osr.SpatialReference()
# GDAL 2.3.3, released 2018/12/14
print(outRasterSRS.ImportFromEPSG(4326))            # return 7, ERROR 6: EPSG PCS/GCS code 4326 not found in EPSG support files.
print(outRasterSRS.SetWellKnownGeogCS("WGS84"))     # return 0
print(outRasterSRS.SetWellKnownGeogCS("EPSG:4326")) # return 7, ERROR 6: EPSG PCS/GCS code 4326 not found in EPSG support files.
outRaster.SetProjection(outRasterSRS.ExportToWkt())

outband.FlushCache()
outband         = None
outRaster       = None

fp = gdal.Open(file)
ds = fp.GetRasterBand(band).ReadAsArray()
# print(ds)
for x in range(ds.shape[0]):
    print((x + 1), ',', ','.join(['{}'.format(d) for d in ds[x]]))

# file = os.path.join(fpath, '../', 'Data', 'examples', 'GTiff.Big.tif')
