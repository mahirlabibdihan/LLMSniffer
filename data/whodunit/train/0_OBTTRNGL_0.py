T = int(input())
for _ in range(T):
    k, A, B = map(int, input().split())
    if A > B:
        A, B = B, A
    if B - A > k // 2:
        print(A + k - B - 1)
    else:
        print(B - A - 1)