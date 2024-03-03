arr=[2,7,11,15]
target=9arr=[2,7,11,15]
target=9
size=len(arr)
indexes=[]
for i in range(size):
   for j in range(i+1,size):
       if arr[i] + arr[j]==target:
           indexes.append(i)
           indexes.append(j)
