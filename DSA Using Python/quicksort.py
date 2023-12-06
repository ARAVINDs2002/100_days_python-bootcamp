def quicksort(arr):
    #94263
    length=len(arr)
    if length<=1:
        return arr
    else:
        pivot=arr.pop()
        lessers=[]
        greaters=[]
        for i in arr:
            if pivot<i:
                greaters.append(i)
            else:
                lessers.append(i)
        return quicksort(lessers)+[pivot]+quicksort(greaters)
def main():
    arr=[2,1,3,4,55,4,67,65,89]
    sorted=quicksort(arr)
    print(sorted)
if __name__ == '__main__':
    main()