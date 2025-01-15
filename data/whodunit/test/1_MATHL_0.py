m=1000000007
f=[1,2,6]
a=[1,2,12]
for i in range(3,10**6):
    f.append((f[i-1]*(i+1))%m)
    a.append((f[i]*a[i-1])%m)
for _ in range(int(input())):
    n=int(input())
    print(a[n-1])