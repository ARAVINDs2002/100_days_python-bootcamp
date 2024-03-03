heights=[1,2,3,4,5]
newlist=[]
size=len(heights)
print(size)
avg=0
for i in heights:
    avg=round(avg+i/size)
    newlist.append(avg)
print(avg)
print(f"new list is {avg}")

