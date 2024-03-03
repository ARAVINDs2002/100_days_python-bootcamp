import numpy as np

vec1=[1,2j]#define & add sub div mul
vec2=[4,5j]
sum=np.add(vec1,vec2)
print(f"addition is {sum}")
dif=np.subtract(vec1,vec2)
print(f"subtraction  is {dif}")
mul=np.multiply(vec1,vec2)
print(f"product  is {mul}")
div=np.divide(vec1,vec2)
print(f"division  is {div}")
#dot
v1=[1,5]
v2=[4,7]
dot=np.dot(v1,v2)
print(f"dot product is {dot}")
#vec scalarmul
vector=[2,3j]
scalar=[1]
vecXscl=np.multiply(vector,scalar)
print(f"vector scalar multiplication is {vecXscl}")