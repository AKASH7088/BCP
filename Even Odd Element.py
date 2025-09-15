#6.
a=[1,2,3,4]
even_count=sum(1 for x in a if x % 2 == 0)
odd_count =len(a)-even_count
print(abs(even_count-odd_count))