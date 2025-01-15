def solve():
    N, c = map(int, input().split())
    l = 1
    r = N
    while l < r:
        mid = (l + r) // 2
        print(1, mid)
        res = int(input())
        if res == 0:
            l = mid + 1
        else:
            print(2)
            r = mid
    print(3, l)

solve()