N = int(input("Enter size of the array: "))

arr = list(map(int, input("Enter array elements: ").split()))

for i in range(N):               # starting index
    for j in range(i, N):        # ending index
        print(*arr[i:j+1])       # print subarray elements
