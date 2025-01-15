T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    a = [0]*n
    b = [0]*n
    for i in range(k):
        a[p[i]-1] = 1
    j = n
    for i in range(n-1, -1, -1):
        if a[i] == 1:
            b[i] = j
            j -= 1
    j = 1
    for i in range(n):
        if a[i] == 0:
            b[i] = j
            j += 1
    if p[0] != b.index(n)+1:
        print("NO")
    else:
        print("YES")
        print(*b)