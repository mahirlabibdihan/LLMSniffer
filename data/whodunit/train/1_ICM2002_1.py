t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    s = sum(l)
    print('YES' if s % k == 0 and s / k >= max(l) else 'NO')