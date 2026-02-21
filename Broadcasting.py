import numpy as np

lst = [100,200,300,400,500]
arr = np.array(lst)
discount = 10
final_arr = arr - (arr * (discount/100))
print(final_arr)

print(arr*2)

#If value are same 3 in 2D 3 in 1D
matrix = np.array([[1,2,3],[4,5,6]])
vector = np.array([1,2,3])

result = matrix + vector
print(result)