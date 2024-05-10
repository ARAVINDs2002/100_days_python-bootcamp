def sum_of_arrays(arr):
    sum=0
    for ele in range(0,len(arr)-1):
        sum+=arr[ele]
    return sum    
arr=[1,100,2,3,4,5,6,7,8,9]
res=sum_of_arrays(arr)
print(res)