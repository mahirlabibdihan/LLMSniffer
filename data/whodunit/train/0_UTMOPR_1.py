T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    S = sum(arr)
    print("odd" if S % 2 == 1 or K == 1 else "even")