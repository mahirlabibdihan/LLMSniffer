def solve():
    T = int(input().strip())
    for _ in range(T):
        N, K = map(int, input().strip().split())
        S = sorted(list(input().strip()))
        ones = S.count('1')
        zeros = S.count('0')
        if ones % (N // K) != 0 or zeros % (N // K) != 0:
            print("IMPOSSIBLE")
        else:
            print(''.join(S))

solve()