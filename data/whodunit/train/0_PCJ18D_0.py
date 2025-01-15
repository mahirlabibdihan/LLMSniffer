T = int(input())
for _ in range(T):
    N, B = map(int, input().split())
    A = (N + B - 1) // B
    print(A)