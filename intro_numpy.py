#numpy array
import numpy as np
lst = [1,2,3,4,5,6,7,8,9]
print(lst)

array = np.array(lst)
print(array)

#1D array
ar_1D = np.array([1,2,3])
print(ar_1D)

#2D array
ar_2D = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])
print(ar_2D)

#3D array (Matrix)
ar_3D = np.array([[[1,2],[3,4]],
                  [[5,6],[7,8]],
                  [[9,10],[11,12]]])
print(ar_3D)