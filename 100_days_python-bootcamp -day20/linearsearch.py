list=[1,2,3,4,5,56,78]
low=list[0]
high=list[1]
key=int(input("ener key :"))
found=False
while low<=high:
    mid=low+high//2
    if key==list[mid]:
        found=True
        print(f"element foud at{mid}")
        break


    elif list[mid]<key:
        high=mid+1
    else:
        low=mid-1
    if not found:
     print("elemnt not found")
     break
