from decimal import *
t=int(input())
while t>0:
    t-=1
    K=int(input())
    if K==0:
        print(3)
    else:
        ans='3.'
        y=33102
        x=103993%y

        for i in range(K):
            x*=10
            ans+=str(x//y)
            x=x%y
        print(ans)