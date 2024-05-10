string = "guiffifff"
target = "gui"

len_str = len(string)
len_tar = len(target)

for i in range(0, len_str - len_tar + 1): 
    for j in range(0, len_tar):
        if string[i + j] != target[j]:
            break
    if j == len_tar - 1: 
        print(f"Found at {i}")
