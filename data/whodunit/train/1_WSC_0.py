for _ in range(int(input())):
    n, m = map(int, input().split())
    a = [0]*n
    for i in range(m):
        l, r = map(int, input().split())
        a[l-1],a[r-1] = 1,1
    print ('NO') if sum(a) > 3 or m > 2 else print ('YES')   