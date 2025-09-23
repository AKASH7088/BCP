#3.....
N=int(input())
lst=[]
M=int(input())
for i in range(N):
    lst.append(int(input()))
for j in range(len(lst)):
    if M==lst[j]:
        print(j)
    elif M!=lst[j]:
        continue
    else:
        print(-1)


