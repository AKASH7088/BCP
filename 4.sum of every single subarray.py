N = int(input("Enter size of the array: "))

arr = list(map(int, input("Enter array elements: ").split()))

for i in range(N):              
    total = 0                    
    for j in range(i, N):       
        total += arr[j]
        print(total)
