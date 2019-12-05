# IHEWAstandard.Architecture

Define the **Architecture standard** of WaterAccounting Tools.

## Architecture

Version 1, [Image](./img/v1/Arch.IHEWA.png)

### Components

  - IHEWAcollect, [Image](./img/v1/Arch.IHEWAcollect.png)
    - Products
  - IHEWAconverter, [Image](./img/v1/Arch.IHEWAconverter.png)
  - IHEWAengine, [Image](./img/v1/Arch.IHEWAengine.png)
    - Plugin, _BMI_, _OpenBMI_
    - Engine 1, Hydrological model
      - WaterPix
      - SurfWAT
      - SWAT+
      - ...
    - Engine 2, ** model
      - Hyperloop
      - ...
  - IHEWAgis, [Image](./img/v1/Arch.IHEWAgis.png)
    - GDAL
  - IHEWAsheet, [Image](./img/v1/Arch.IHEWAsheet.png)
    - SVG
    - PDF
    - CSV
    - Image
  - _IHEWAmobile_, [Image](./img/v1/Arch.IHEWAmobile.png)
    - _Android_
    - _iOS_

