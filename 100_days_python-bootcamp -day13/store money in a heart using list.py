matrix = [['❤️','❤️','❤️'],
          ['❤️', '❤️', '❤️'],
          ['❤️','❤️', '❤️']]

"""print(matrix[0])
print(matrix[1])
print(matrix[2])"""
print(f"{matrix[0]}\n{matrix[1]}\n{matrix[2]}")

row = int(input("Enter row no of the heart to store money: "))
col = int(input("Enter colno of the heart to store money: "))

matrix[row][col] = "💵"
print(matrix[0])
print(matrix[1])
print(matrix[2])