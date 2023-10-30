height=[124,321,432,512]
count=0
for i in height:#for findiong the number of persons in list
  count=count+1
print(f"there are {count} persons in the list")  
sum=0
for i in height:#for sum
  sum+=i
print(f"the sum of height is {sum}")  
#for avg
avg=sum//count
print(f"average is {avg}")