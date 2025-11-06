N = int(input("Enter size of the array: "))

arr = list(map(int, input("Enter array elements: ").split()))

total_sum = 0
for i in range(N):
    total_sum += arr[i] * (i + 1) * (N - i)

print(total_sum)
