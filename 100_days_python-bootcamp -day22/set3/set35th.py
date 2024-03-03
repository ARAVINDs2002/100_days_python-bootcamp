import numpy as np

# Define the matrix A
A = np.array([[3, 1],
              [1, 2]])

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# Print eigenvalues and eigenvectors
print("Eigenvalues:")
print(eigenvalues)
print("\nEigenvectors:")
print(eigenvectors)

# Reconstruct the matrix using eigenvectors and eigenvalues
reconstructed_matrix = np.dot(np.dot(eigenvectors, np.diag(eigenvalues)), np.linalg.inv(eigenvectors))
print("old matrix is:\n")
print(A)
# Print the reconstructed matrix
print("\nReconstructed Matrix:")
print(reconstructed_matrix)
