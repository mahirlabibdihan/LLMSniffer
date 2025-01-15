t=int(input())
for _ in range(t):
    n=input()
    lis=list(map(int,input().split()))
    lis.append(-1)
    lis.sort()
    lis.append(-1)
    count=0
    for i in range(1,len(lis)-1):
        if (( lis[i+1] == lis[i]+1 )  or  ( lis[i-1] == lis[i]-1)):
            x=0
        else:
            lis[i]=lis[i]+1
            count=count+1 
    print(count)
        