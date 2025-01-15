t=int(input())
while t:
    n=int(input())
    for i in range(n-int(n/2),2*n-int(n/2)):
        print(i,end=' ')
    print('')
    t-=1