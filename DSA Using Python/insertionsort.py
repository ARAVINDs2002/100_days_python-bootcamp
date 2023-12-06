def ins(arr):
    for i in range(1, len(arr)):
        
        while arr[i - 1] > arr[i] and i > 0:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i = i - 1

def main():
    arr = [32, 3, 5, 1, 4, 3, 2, 3, 4, 5, 4]
    ins(arr)  # Sort the array in-place
    print(arr)

if __name__ == "__main__":
    main()
