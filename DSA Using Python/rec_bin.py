def bin_search(arr, low, high, key):
    
   
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            
            print("found")
            
        elif arr[mid] < key:
            found = bin_search(arr, mid + 1, high, key)
        else:
            found = bin_search(arr, low, mid - 1, key)
    
    else:
        print("not found")

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
size = len(arr)
low = 0
high = size - 1
key = 1

bin_search(arr, low, high, key)
