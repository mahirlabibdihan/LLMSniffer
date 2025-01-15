T = int(input())
for _ in range(T):
    n1, n2, m = map(int, input().split())
    total = min(n1, n2, m*(m+1)//2)
    print(n1 + n2 - 2*total)