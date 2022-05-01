import numpy as np

# create a length-10 integer array filled with zeros
print(np.zeros(10, dtype=int))

print()

# creating a 3x5 floating-point array filled with 1s
print(np.ones((3, 5), dtype=float))

print()

# create a 3x5 array filled with np.pi
print(np.full((3, 5), np.pi))

print()

# create an array with a linear sequence
print(np.arange(0, 20, 2))

print()

# five values evenly spaced between 0 and 1
print(np.linspace(0, 1, 5))

print()

# create a 3x3 identity matrix
print(np.eye(3))
