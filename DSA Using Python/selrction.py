def selection(arr,size):
    min=0
    for i in range(0,size-1):
        for j in range(i+1,size):
            if(arr[j]<arr[i]):
                arr[j],arr[i]=arr[i],arr[j]
    print(arr)         
                
            
    
    
    
    
    
arr=[2,1,3,2,3,2,4,5,4,6,7,5,4,3,2,5,7] 
size=len(arr)
res=selection(arr,size)   
print(res)