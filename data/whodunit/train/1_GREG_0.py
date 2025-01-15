def sieve(n):
    prime = [i for i in range(n+1)]
    prime[0]=True
    prime[1]=True
    p = 2
    while (p * p <= n):
        if (prime[p] != True):
            for i in range(p * p, n+1, p):
                prime[i] = True
        p += 1
    prime=list(set(prime))

    del prime[0]
    
    return prime

n,m=map(int,input().split())
print(len(sieve(n+m)))
