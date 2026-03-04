import numpy as np

data = np.array([
    [25, 30, 45, -999, 50],
    [27, np.nan, 47, 52, 49],
    [29, 31, 2000, 48, 51],
    [-10, 33, 46, 49, np.nan],
    [26, 29, 44, 47, 50],
    [28, 32, -999, 46, 52],
    [30, 34, 48, 1000, 53],
    [np.nan, 35, 49, 50, 54],
    [31, 36, 47, 48, -999],
    [32, 37, 46, 49, 55]
])

data[data < 0] = 0
data[np.isnan(data)] = np.nanmean(data)
data[data >= 1000] = np.nanmean(data)

print(data)