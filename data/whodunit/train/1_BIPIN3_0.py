
t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    m = (10**9)+7
    d=((k%m)*pow(k-1,n-1,m)%m)
    print(d)
