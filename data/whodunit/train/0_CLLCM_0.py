T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    if all(a % 2 == 1 for a in A):
        print("YES")
    else:
        print("NO")