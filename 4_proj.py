import numpy as np

np.set_printoptions(suppress=True)
data = np.genfromtxt(
    "Z_Data2.csv",
    delimiter=",",
    skip_header=1,
    dtype=float,
    encoding="utf-8"
)
print("EmpID,Age,Experience,Salary,Bonus,Department_Rating")
print(data[:5])

data[data[:,1] < 18, 1] = np.nanmean(data[:,1])

rows_to_delete = np.where(data[:,2] <= 2)[0]
data = np.delete(data, rows_to_delete, axis=0)

data[data[:,3]< 0] = np.mean(data[:,3])
data[np.isnan(data[:,3]), 3] = np.nanmean(data[:,3])
data[data[:,4]< 0,4] = np.nanmean(data[:,4])

data = data[~np.isnan(data[:,0])]

np.savetxt(
    "Z_Data2_edited.csv",
    data,
    delimiter=",",
    fmt="%.0f",
    header="EmpID,Age,Experience,Salary,Bonus,Department_Rating",
    comments=""
)