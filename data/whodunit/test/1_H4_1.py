def S(a, n, m):
    if n == -1: return 0
    if n == 0: return 1
    if n == 1: return (1 + a) % m 
    if n % 2 == 1: return ((1 + a) * S(a * a % m, (n - 1)//2, m))%m
    else: return (1 + a * (1 + a) * S(a * a % m, n//2 - 1, m) )%m  
for _ in range(int(input())):
    n,m = map(int,input().split(' '));s=0;e = n//m
    for i in range(1,n%m+1):s += pow(i,e*m + i,m);s = s%m
    for i in range(2,m+1):s += (((S(pow(i,m,m),e-1,m) )%m)*pow(i,i,m))%m;s = s%m
    print((s+e)%m)    