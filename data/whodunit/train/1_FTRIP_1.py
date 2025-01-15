for _ in range(int(input())):

    S, N, M, K = map(int, input().split())
    
    
    def cnk(n, k):
        k_min = min(k, n - k)
        num, denom = 1, 1
    
        for x in range(1, k_min + 1):
            num *= (n - x + 1)
            denom *= x
        return num // denom
    
    
    total = cnk(S - 1, N - 1)
    upper_lim = min(M, N)
    
    num = 0
    for k in range(K, upper_lim + 1 - 1):
        if (S - M) >= (N - k - 1):
            num += cnk(M - 1, k) * cnk(S - M, N - k - 1)
    ans = num / float(total)
    print("%.9f" % ans)
