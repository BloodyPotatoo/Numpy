import numpy as np

# Messy dataset (students marks)
data = np.array([
    [101, 85, 90, np.nan],
    [102, 78, -1, 88],
    [103, np.nan, 76, 95],
    [104, 92, 89, "absent"],
    [105, 67, 72, 70],
    [106, 105, 81, 79],   # 105 is invalid (marks >100)
    [107, 74, 68, None]
], dtype=object)

print(data)

data[data == "absent"] = np.nan
data[data == "None"] = np.nan

data = data.astype(float)
data[data > 100] = 100
data[data < 0] = 0
#mean of data ignoring nan
mean_value = np.nanmean(data)

# replace all NaN with that mean
data[np.isnan(data)] = mean_value
print(data)
