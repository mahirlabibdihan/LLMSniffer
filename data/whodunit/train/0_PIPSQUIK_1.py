def solve(N, H, Y1, Y2, L, barriers):
    count = 0
    for t, X in barriers:
        if L == 0:
            break
        if (t == 1 and X <= H - Y1) or (t == 2 and X <= Y2):
            count += 1
        else:
            L -= 1
            if L > 0:
                count += 1
    return count

T = int(input())
for _ in range(T):
    N, H, Y1, Y2, L = map(int, input().split())
    barriers = [list(map(int, input().split())) for _ in range(N)]
    print(solve(N, H, Y1, Y2, L, barriers))