import numpy as np

#Indexing in numpy arrays
arr = np.array([1,2,3,4,5,6,7,8,9])
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[-1])

#Slicing
"""
arr[start:stop(excluded):step]
"""
print(arr[1:5])
print(arr[0:-1])
print(arr[::-1])
print(arr[::2])
