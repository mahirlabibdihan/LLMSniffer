def solve():
    T = int(input().strip())
    for _ in range(T):
        N, K = map(int, input().strip().split())
        A = list(map(int, input().strip().split()))
        A.append(0)
        A.append(0)
        ans = 1
        cnt = 1
        mx = -1
        for i in range(1, N+1):
            if A[i] > K and A[i-1] > K:
                cnt = 1
                mx = max(mx, A[i])
            elif A[i] > K:
                cnt = 1
                mx = A[i]
            elif A[i] == K or A[i] > mx:
                cnt += 1
                mx = max(mx, A[i])
            else:
                cnt = 1
            ans = max(ans, cnt)
        print(ans)

solve()