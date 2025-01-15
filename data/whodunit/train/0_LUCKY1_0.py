def solve(n):
    ans = [0]*(n+1)
    f4 = [0]*(n+1)
    f7 = [0]*(n+1)
    cnt = [0]*(n+1)
    for i in range(1, n+1):
        f4[i] = f4[i-1]
        f7[i] = f7[i-1]
        if '4' in str(i):
            f4[i] += 1
        if '7' in str(i):
            f7[i] += 1
        cnt[i] = cnt[i-1]
        if f4[i] == f7[i]:
            cnt[i] += 1
        ans[i] = ans[i-1] + cnt[i]
    return ans[n]

T = int(input())
for _ in range(T):
    N = int(input())
    print(solve(N))