list=[[100,32,45,32,76,879,54,46,21,44,1,43],
      [1,2,3,4,5],
      [5,4,3,2,1],
      [],
      [1]]
size=len(list)
for i in range(size):
    min_index=i
    for j in range(i+1,size):
        if list[j]<list[min_index]:
            min_index=j
    list[i],list[min_index]=list[min_index],list[i]
for arr in list:
   print(arr)


