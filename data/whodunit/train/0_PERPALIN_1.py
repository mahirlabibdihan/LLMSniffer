T = int(input())
for _ in range(T):
    N, P = map(int, input().split())
    if P == 1 or P == 2:
        print("impossible")
    else:
        base = "ab" * (P // 2) + "a" * (P % 2)
        print((base + base[::-1]) * (N // (2 * P)))