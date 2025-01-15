T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    if N % 2 == 0 or M % 2 == 0:
        print("Ari")
    else:
        print("Rich")