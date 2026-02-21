import numpy as np

#concetenate(ADD)
arr_1 = np.array([1,2,3])
arr_2 = np.array([4,5,6])

new_arr = np.concatenate((arr_1, arr_2), axis=0)
print(new_arr)

#Remove
a = np.delete(arr_1,0)
print(a)

arr_3 = np.array([[1, 2], [3, 4]])
b = np.delete(arr_3,0,axis = 0)
print(b)