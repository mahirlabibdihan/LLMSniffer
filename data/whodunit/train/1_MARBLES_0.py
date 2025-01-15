for _ in range(int(input())):
    
    n,k = map(int,input().split()); n -= 1; k -=1; k = min(k,n-k); ans = 1
    
    for i in range(k):
        ans *= (n-i)
        ans //= (i+1)
    
    print(ans)
