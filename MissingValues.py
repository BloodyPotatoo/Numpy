import numpy as np

#by default nan value is 0 if nan_to_num is used
arr = np.array([1,2,3,np.nan,5,6])
print(np.isnan(arr))
clear_arr = np.nan_to_num(arr,nan = 4)
print(clear_arr)

#Inf functions
arr2 = np.array([1,2,3,np.inf,-np.inf,5])
clear_arr2 = np.isinf(arr2)
print(clear_arr2)

clear_arr3 = np.nan_to_num(arr2, posinf = 100, neginf = -100)
print(clear_arr3)