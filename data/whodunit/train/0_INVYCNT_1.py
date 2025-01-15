T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    inversions = sum(1 for i in range(N) for j in range(i+1, N) if A[i] > A[j]) * K
    print(inversions)