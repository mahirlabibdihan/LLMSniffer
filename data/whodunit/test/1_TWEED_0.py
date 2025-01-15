t=int(input())
for i in range(t):
    n,c=input().split()
    a=list(map(int,input().split()))
    n=int(n)
    if n==1 and a[0]%2==0 and c=='Dee':
        print("Dee")
    else:
        print("Dum")