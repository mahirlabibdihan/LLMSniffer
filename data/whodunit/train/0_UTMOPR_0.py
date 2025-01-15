T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    S = sum(arr)
    if S % 2 == 0:
        if K == 1:
            print("odd")
        else:
            print("even")
    else:
        print("odd")