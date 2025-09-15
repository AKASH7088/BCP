#10.reverse
a=[3,5,1,2,1,2]
rev=[]
for i in range(len(a)-1,-1,-1):
    rev.append(a[i])
print(rev)