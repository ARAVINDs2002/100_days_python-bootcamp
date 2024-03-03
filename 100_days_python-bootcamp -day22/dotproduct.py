import numpy as np


matrix1 = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])



matrix2 = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])


result = np.dot(matrix1 ,matrix2)

# Print the result
print("Result of Scalar Matrix Multiplication:")
print(result)