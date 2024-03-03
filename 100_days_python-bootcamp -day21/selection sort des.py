arr=[1,2,3,4,5]
size=len(arr)
for i in range(size-1,0,-1):
    for j in range(i):
        if arr[j]<arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)



