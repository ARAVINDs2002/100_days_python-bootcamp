import numpy as np

# Create a matrix
matrix = np.array([[1,0,0,0,0],
                   [0,1,0,0,0],
                   [0,0,1,0,0],
                   [0,0,0,1,0],
                   [0,0,0,0,1]])


transposed_matrix = np.transpose(matrix)


result_matrix = np.dot(transposed_matrix, matrix)


identity_size = matrix.shape[0]


identity_matrix = np.identity(identity_size)


is_orthogonal = np.all(result_matrix == identity_matrix)

if is_orthogonal:
    print("The matrix is orthogonal.")
else:
    print("The matrix is not orthogonal.")
