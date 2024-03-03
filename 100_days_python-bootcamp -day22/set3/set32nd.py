import numpy as np


matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])


rank = np.linalg.matrix_rank(matrix)


print("Rank of the matrix is:", rank)
