T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    inversions = 0
    for i in range(N):
        for j in range(i+1, N):
            if A[i] > A[j]:
                inversions += 1
    total_inversions = inversions * K
    print(total_inversions)