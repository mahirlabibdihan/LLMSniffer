from collections import Counter

T = int(input())
for _ in range(T):
    R, S = input().split()
    if Counter(R) == Counter(S):
        print("YES")
    else:
        print("NO")