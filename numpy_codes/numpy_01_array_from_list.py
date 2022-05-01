import numpy as np

print(np.__version__)

# creating array from the list
a = [4, 5, 6, 7, 8]
array = np.array(a)

print(array)  # array
print(array.ndim)  # dimension of the n-dimensional array
print(array.dtype)  # data types of the elements in the array
print(array.shape)  # shape of the array

# multiple data type in the array
# so, it makes all the data type to the same type, that is more upcasting

print(np.array([3.14, 4, 5, 6, 9]))

# explicitly set the data
print(np.array(a))

print(np.array(a, dtype='float32'))  # explicitly set the data elements as desired

# 2D array introduction
a = [range(i, i + 3) for i in [2, 4, 6]]
print(np.array(a))


