def solve(k, A, B):
    if A > B:
        A, B = B, A
    if B - A > k // 2:
        return A + k - B - 1
    else:
        return B - A - 1

T = int(input())
for _ in range(T):
    k, A, B = map(int, input().split())
    print(solve(k, A, B))