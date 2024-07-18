import numpy as np

# 1D array - Vector
one = np.array([1, 2, 3])
print(type(one))
print(one)
print("================")

# 2D array - Matrix
two = np.array([[1, 2], [3, 4]])
print(two)
print("================")

# 3D array - Tensor
three = np.array([[[1, 2], [3, 4], [5, 6]]])
print(three)
print("================")

# dtype for specefic data type
print(np.array([1,2,3],dtype=int))
print(np.array([1,2,3],dtype=bool))
print("================")

# arange()
print(np.arange(1,10))
print("================")

# reshape()
print(np.arange(1,10).reshape(3,3))
print("================")

#np.ones
print(np.ones((3,4)))
print("================")

#np.zeros
print(np.zeros((2,3)))
print("================")

#np.randon
print(np.random.random((3,2)))
print("================")

#np.linspace
print(np.linspace(1,10,5))
print("================")

#np.identity
print(np.identity(5))
