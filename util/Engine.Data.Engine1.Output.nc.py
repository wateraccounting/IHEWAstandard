import os

import datetime
import numpy as np
import pandas as pd
import xarray as xr

# print(os.getcwd())
# print(os.path.dirname(os.path.abspath(__file__)))
fpath = os.path.dirname(os.path.abspath(__file__))

# %% Engine1.Output.nc
file = os.path.join(fpath, '../', 'Engine', 'examples', 'Engine1.Output.nc')
