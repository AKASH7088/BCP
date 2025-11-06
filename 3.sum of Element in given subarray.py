N = int(input("Enter size of the array: "))

arr = list(map(int, input("Enter array elements: ").split()))

L, R = map(int, input("Enter L and R: ").split())

subarray_sum = sum(arr[L-1:R])

print(subarray_sum)
