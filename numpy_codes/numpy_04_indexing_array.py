import numpy as np

x1 = np.array([5, 0, 3, 3, 7, 9])

print(x1)

# accessing the single element
print(f"first element: {x1[0]} and the 4-th element: {x1[3]}")

# index from the end of the array
print(f"Last element is: {x1[-1]}")
print(f"Second Last element is: {x1[-2]}")

print()

# for multi-dimensional array
x2 = np.array([
    [3, 5, 2, 4],
    [7, 6, 8, 8],
    [1, 5, 6, 3]
])

print(x2)

print(x2[0])
print(x2[0, 0])


# modify the value
x2[0, 0] = 50

print(x2)