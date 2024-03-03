def fact(a):
   if(a==0 or a<0):
       return 1
   else:
       return a * fact(a-1)


def main():
    a=int(input("enter the num"))
    b=fact(a)
    print(b)

main()
