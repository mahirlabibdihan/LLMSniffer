T=int(input())
for i in range(T):
    k=int(input())
    N=input().split(' ')
    x=1/2
    for j in range(k):
        x=x*2-int(N[j])
    if(x==0):
        print('Yes')
    else:
        print('No')