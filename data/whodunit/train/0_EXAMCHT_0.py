import math
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    if A == B:
        print(-1)
    else:
        print(gcd(abs(A-B), min(A,B)))