T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    a.append(360)
    diff = [a[i+1] - a[i] for i in range(n)]
    min_diff = min(diff)
    print(360//min_diff - n)