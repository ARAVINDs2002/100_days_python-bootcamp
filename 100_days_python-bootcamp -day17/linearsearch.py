#linear search
def linearsearch(list,key):
    flag=0
    for i in range(len(list)):
        if key in list:
            flag=1
        else:
            flag=2
    if flag==1:
       print("found")
    else:
       print("not found")


def main():
    list=[1,2,3,4,6,41,33,98,7,8,86,568,9,5]
    key=int(input("enter the search element :"))
    linearsearch(list,key)
main()