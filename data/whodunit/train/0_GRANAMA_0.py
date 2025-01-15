T = int(input())
for _ in range(T):
    R, S = input().split()
    if sorted(R) == sorted(S):
        print("YES")
    else:
        print("NO")