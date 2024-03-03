list=[16,22,3,45,6,7,90]
size=len(list)
for i in range(size):
    min=i
    for j in range(i+1,size):
        if list[j]<list[min]:
            min=j
    list[i],list[min]=list[min],list[i]
print(list)

