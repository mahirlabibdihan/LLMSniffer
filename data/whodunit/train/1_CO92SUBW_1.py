from bisect import bisect_left
x=[0]*50000
for i in range(50000):
    x[i] = x[i - 1] + (i + 1)
for j in range(int(input())):
    n=int(input())
    if(n==1):
        print(1)
    else:
        index=bisect_left(x,n)
        a=index
        b=index-1
        c=b+abs(x[b]-n)+1
        d=a+abs(x[a]-n)+1
        print(min(c,d))





