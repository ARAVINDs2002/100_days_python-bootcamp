arr=[1,2,3,4,5,6,7]
low=0
high=len(arr)-1
key=int(input(" enter the key"))
found=False
while low<=high:
    mid=(low+high)//2
    if arr[mid]==key:
        found=True
        print(f"found at {mid}")
        break
    elif arr[mid]<key:
        low=mid+1
    else:
        high=mid-1
if not found:
    print("not here'")
