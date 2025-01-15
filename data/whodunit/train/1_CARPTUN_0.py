t=int(input())
for testcase in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    C,D,S=list(map(int,input().split()))
    x=((C-1)*max(a))+sum(a)
    time=x-sum(a)
    print(time)