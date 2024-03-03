a=int(input("enter the number 1: "))
b=int(input("enter the number 2: "))
c=input("enter the operartion")
if c =='+':
    add=a+b;
    print("sum is "+str(add))
elif c =='-':
    dif=b-a;
    print("difference is"+str(dif))
elif c=='*':
    mul=b*a;
    print("multiplication is :"+mul)
elif c=='/':
    div=a/b;
    print("division is"+str(div))
else:
        print("sorry")

