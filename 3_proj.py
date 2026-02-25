import numpy as np
import pandas as pd

np.set_printoptions(suppress=True)
data = np.loadtxt("/Users/user/OneDrive/Desktop/Python/Numpy/Z_data.csv",
                     delimiter=",",
                     skiprows=1,)
                     
print(data[:5])

max_salary = np.max(data[:, 1])
print(f"Max salary: ", max_salary)
data[data == 0] = np.mean(data[:, 1])
print(f"Minimum salary: ", np.min(data[:, 1]))

np.savetxt(
    "Z_data_edited.csv",
    data,
    delimiter=",",
    fmt="%.0f",
    header="Age,Salary,Experience_Years,Performance_Score",
    comments=""
)