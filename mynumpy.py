import numpy as np

arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(arr.shape)
print(arr)
print(arr.ndim)

arr2=arr.reshape(2,6)
print("shape 2:", arr2.shape)
print("dim 2:", arr2.ndim)



