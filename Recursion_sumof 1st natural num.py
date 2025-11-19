def digitSum(n):
    if(n==0):
        return 0
    digit =n%10
    n=n//10
    return digitSum(n)+digit
n=int(input())
print(digitSum(n))
