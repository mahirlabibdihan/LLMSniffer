mod=10**9+7
n=int(input())
k=int(input())
den=pow(2,n-1)
num=pow(2,n-1)-n
ans=(pow(den,mod-2,mod)*num)%mod
print(ans)