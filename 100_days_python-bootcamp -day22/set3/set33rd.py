import numpy as np

# Define your matrix
matrix = np.array([[1, 0, 0, 0],
                   [0, 0, 2, 0],
                   [0, 0, 0, 0],
                   [0, 3, 0, 4]])

# Calculate the total number of elements in the matrix
total_elements = matrix.size

# Calculate the number of zero elements
zero_elements = np.count_nonzero(matrix == 0)

# Calculate the sparsity
sparsity = zero_elements / total_elements

# Print the sparsity
print("Sparsity of the matrix:", sparsity)
