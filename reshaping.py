import numpy as np

#Reshaping to 2D or 3D
arr = np.array([1,2,3,4,5,6,7,8,9])
reshaped_arr_1 = arr.reshape(3,3)
print(reshaped_arr_1)
reshaped_arr_2 = arr.reshape(1,9)
print(reshaped_arr_2)

#Rehsaping form 3D to 1D
#.ravel = affect original
#.flatten = copy
arrr = np.array([[1,2],[3,4],[5,6]])
print(arrr.flatten())
print(arrr.ravel())