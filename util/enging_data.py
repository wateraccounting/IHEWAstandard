import os

import numpy as np
import pandas as pd
import xarray as xr

ds = xr.Dataset(
    {
        'foo': (('x', 'y'), np.random.rand(4, 5))},
        coords={'x': [10, 20, 30, 40],
        'y': pd.date_range('2000-01-01', periods=5),
        'z': ('x', list('abcd'))
    }
)

print(os.getcwd())
print(os.path.dirname(os.path.abspath(__file__)))

fpath = os.path.dirname(os.path.abspath(__file__))
ds.to_netcdf(os.path.join(fpath, '../', 'Engine', 'examples', 'Engine2.Input.nc'))
