numbers = input("Enter a list of numbers separated by spaces: ")
num_list = numbers.split()
length = len(num_list)



for i in range(length):
   num_list[i] = int(num_list[i])

max_num = num_list[0]


for i in num_list:
   if i > max_num:
      max_num = i

print(f"The maximum number is: {max_num}")

