def solve():
    T = int(input().strip())
    for _ in range(T):
        N, K = map(int, input().strip().split())
        S = sorted(list(input().strip()))
        if S.count('1') % (N // K) != 0 or S.count('0') % (N // K) != 0:
            print("IMPOSSIBLE")
        else:
            print(''.join(S))

solve()