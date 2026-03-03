import numpy as np
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([50,60,70,80,90])
result = arr1 + arr2
print(result)
print(result.shape)
print(result.size)
print(result.ndim)
print(result.dtype)


mat1 = np.array([[2,3,4],[2,3,4]])
           
mat2 = np.array([[4,5,6],[4,5,6]])

print(np.dot(mat1, mat2.T))
print(mat1 * mat2)






