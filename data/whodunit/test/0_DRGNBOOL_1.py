def solve():
    N, M = map(int, input().split())
    soints = [0]*101
    sofloats = [0]*101
    for _ in range(N):
        C, L = map(int, input().split())
        soints[L] += C
    for _ in range(M):
        C, L = map(int, input().split())
        sofloats[L] += C
    ans = 0
    for i in range(101):
        if sofloats[i] > soints[i]:
            ans += sofloats[i] - soints[i]
    print(ans)

T = int(input())
for _ in range(T):
    solve()