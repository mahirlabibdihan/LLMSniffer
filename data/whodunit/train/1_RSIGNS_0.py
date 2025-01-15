def get_power(n,m,D):
    if(n==0):
        return 1
    elif(n==1):
        return 2
    elif(n in D):
        return D[n]
    else:
        D[n] = ((get_power(n//2,m,D)%m)*(get_power(n-n//2,m,D)%m))%m
        return D[n]

T = int(input())
ans = []
m = 10**9 + 7

for _ in range(T):
    K = int(input())

    ans.append( (get_power(K,m,{})*5)%m )

for i in ans:
    print(i)
