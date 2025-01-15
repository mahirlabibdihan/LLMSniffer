T = int(input())
for _ in range(T):
    N, P = map(int, input().split())
    if P == 1 or P == 2:
        print("impossible")
    else:
        print(("ab" * (P // 2) + "a" * (P % 2) + "b" * (P // 2) + "a" * (P % 2)) * (N // P))