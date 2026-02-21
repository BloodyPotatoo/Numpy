import numpy as np

#This shows that there are 3 rows and 3 column
array_2d = np.array([[1,2,3],
                    [4,5,6],
                    [7,8,9]])

print(array_2d.shape)

#This shows the total elements in this array
x = array_2d.size
print(x)

#This shows that how many dimensions are there in this array
array_1d = np.array([1,2,3])
array_3d = np.array([[[1],[2],[3]]])

print(array_1d.ndim)
print(array_2d.ndim)
print(array_3d.ndim)

#This shows the data type of elements in array
z = array_2d.dtype
print(z)

lst = [1,2,3,4,5,6,7,8,9]
q = np.array(lst)
q_str = q.astype(str)
print(q_str)
print(q_str.dtype)
