arr=[1,2,3,4,5]
size=len(arr)
for i in range(size):
    min_index=i
    for j in range(i+1,size):
        if arr[j]>arr[min_index]:
            min_index=j
    arr[i],arr[min_index]=arr[min_index],arr[i]
print(arr)



