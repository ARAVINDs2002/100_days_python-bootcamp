m1=[[1,2,3],
    [4,5,6],
    [7,8,9]]
m2=[[1,2,3],
    [4,5,6],
    [7,8,9]]
res=[[0,0,0],
     [0,0,0],
     [0,0,0]]
for i in range(len(m1)):
   for j in range(len(m2)):
       for k in range(len(m2)):
        res[i][j]+=m1[i][k]*m2[k][j]
print("multipled matrix\n")
for i in res:
    for ele in i:
     print(ele,end="\t")
    print()
