import numpy as np

arr = np.array([1,2,3])
arr2 = np.array([4,5,6])

a = np.vstack((arr, arr2))
b = np.hstack((arr, arr2))
print(a)
print(b)