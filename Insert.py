import numpy as np

#Inser in 1D
arr = np.array([1,2,3,4,5,6,7,8,9])
print(arr)
new_arr = np.insert(arr, 1, 20)
print(new_arr)

#Inster in 2D
arr2 = np.array([[1,2],[3,4],[5,6],[7,8]])
new_arr2 = np.insert(arr2, 1, [9,10], axis = 0)
print(new_arr2)