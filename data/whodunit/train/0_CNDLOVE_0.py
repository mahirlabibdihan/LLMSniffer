T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    if sum(A) % 2 == 0 and max(A) <= sum(A) // 2:
        print("YES")
    else:
        print("NO")