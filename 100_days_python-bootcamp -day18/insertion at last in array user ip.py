list=[1,2,3,34,5,6,7,8]

num=int(input("enter the search element  :" ))
for i in list:
    if num in list:

        print(f"found at pos{i}")
        break
    else:

        print(f"not found !!")
        break

