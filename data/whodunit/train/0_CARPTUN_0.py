T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    C, D, S = map(int, input().split())
    print(max(A) * (C - 1))