T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    if N*M % 2 == 0:
        print("Yes")
    else:
        print("No")