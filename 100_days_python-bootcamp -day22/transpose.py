arr = [[0] * 2 for _ in range(3)]

print("Enter the array elements (3x2 matrix):")
for i in range(3):
    for j in range(2):
        arr[i][j] = int(input())

print("Original matrix:")
for i in range(3):
    for j in range(2):

        print(arr[i][j], end="\t")
    print()

print("Printing matrix transpose:")
for i in range(2):
    for j in range(3):
        print(arr[j][i], end="\t")
    print()