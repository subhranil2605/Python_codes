import numpy as np

np.random.seed(0)  # seed for reproducibility

x1 = np.random.randint(10, size=6)  # one-dimensional array
x2 = np.random.randint(10, size=(3, 4))  # two-dimensional array
x3 = np.random.randint(10, size=(3, 4, 5))  # three-dimensional array

# the number of dimensions
print(f"Dimension of x1: {x1.ndim}")
print(f"Dimension of x2: {x2.ndim}")
print(f"Dimension of x3: {x3.ndim}")

print()

# shape
print(f"Shape of x1: {x1.shape}")
print(f"Shape of x2: {x2.shape}")
print(f"Shape of x3: {x3.shape}")

print()

# total size of the array
print(f"Size of x1: {x1.size}")
print(f"Size of x2: {x2.size}")
print(f"Size of x3: {x3.size}")
