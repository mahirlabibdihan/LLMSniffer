from math import gcd
T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    if A == B:
        print(-1)
    else:
        print(gcd(abs(A-B), min(A,B)))