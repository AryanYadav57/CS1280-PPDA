import numpy as np

# Create two 3x3 matrices with random integers between 1 and 10
matrix1 = np.random.randint(1, 11, (3, 3))
matrix2 = np.random.randint(1, 11, (3, 3))

print("Matrix 1:\n", matrix1)
print("Matrix 2:\n", matrix2)

# Perform matrix subtraction
subtraction_result = matrix1 - matrix2
print("Subtraction Result:\n", subtraction_result)

# Perform element-wise division, handling division by zero
with np.errstate(divide='ignore', invalid='ignore'):
    division_result = np.divide(matrix1, matrix2)
    division_result[np.isnan(division_result)] = 0  # Replace NaN values with 0

print("Element-wise Division Result:\n", division_result)
