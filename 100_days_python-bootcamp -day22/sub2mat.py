# Initialize two 2x2 matrices
arr1 = [[0 for _ in range(2)] for _ in range(2)]
arr2 = [[0 for _ in range(2)] for _ in range(2)]

# Input values for the first matrix
print("Matrix 1 elements:")
for i in range(2):
    for j in range(2):
        while True:
            try:
                arr1[i][j] = int(input(f"Enter element at row {i + 1}, column {j + 1}: "))
                break  # Break out of the loop if input is a valid integer
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

# Input values for the second matrix
print("Matrix 2 elements:")
for i in range(2):
    for j in range(2):
        while True:
            try:
                arr2[i][j] = int(input(f"Enter element at row {i + 1}, column {j + 1}: "))
                break  # Break out of the loop if input is a valid integer
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

# Initialize the result matrix with zeros
arr3 = [[0 for _ in range(2)] for _ in range(2)]

# Perform matrix addition
for i in range(2):
    for j in range(2):
        arr3[i][j] = arr1[i][j]-arr2[i][j]


# Print the result matrix (matrix addition)
print("Matrix subtraction result:")
for i in range(2):
    for j in range(2):
        print(arr3[i][j], end="\t")
    print()  # Move to the next row
