for _ in range(int(input())):
    N,K = map(int,input().split())
    G = list(map(int,input().split()))
    ans = 0
    for i in G:
        Rem = i%K
        if i < K:
            ans += (K-Rem)
        else:
            ans += min(Rem,K-Rem)
    print(ans)