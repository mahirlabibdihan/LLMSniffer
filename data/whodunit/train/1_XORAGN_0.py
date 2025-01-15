t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    x=0
    for j in range(len(a)):
        x=x^(2*a[j])
    print(x)    
