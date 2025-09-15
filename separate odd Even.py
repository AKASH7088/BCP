s=[1,2,3,4,5]
odds=[x for x in s if x % 2 !=0]
evens=[x for x in s if x % 2==0]
print(*odds)
print(*evens)