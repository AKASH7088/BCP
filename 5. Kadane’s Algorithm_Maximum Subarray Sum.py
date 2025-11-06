N = int(input("Enter size of the array: "))

arr = list(map(int, input("Enter array elements: ").split()))

max_ending_here = arr[0]
max_so_far = arr[0]

for i in range(1, N):
    max_ending_here = max(arr[i], max_ending_here + arr[i])
    max_so_far = max(max_so_far, max_ending_here)

print(max_so_far)
