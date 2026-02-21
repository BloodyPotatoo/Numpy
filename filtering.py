import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9])

print(arr[arr<6])
print(arr[(arr>3) & (arr<8)])