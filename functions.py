import numpy as np
lst = [1,2,3,4,5,6,7,8,9]

#Its zeros method where we are printing 0 for 3 times
a = np.zeros(3)
print(a)

#Its ones method where we are printing 1 for a 2by3 matrix which is given as a tuple
b = np.ones((2,3))
print(b)

#Its a full method where we are printing 3 for a 2by2 matrix with a given value 3
c = np.full((2,2), 3)
print(c)

#Its a arrange method where we are printing values from 1 to 11 with a difference of 2 (Remember class 10th/11th AP or sequence)
#Its a arrange method
d = np.arange(1,12,2)
print(d)

#Its a eye method where we are printing a 3by3 matrix with diagonal elements as 1 and rest as 0
e = np.eye(3)
print(e)
f = np.eye(3, 2)
print(f)
g = np.eye(5)
print(g)