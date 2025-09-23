#2...
x=int(input())
k=0
for i in range(1,x+1):
    for j in range(k+1,i+k+1):
        print(j,end=" ")
        k=j
    print()