def solve():
    N, c = map(int, input().split())
    l = 1
    r = N
    while l < r:
        mid = (l + r + 1) // 2
        print(1, mid)
        res = int(input())
        if res == 0:
            l = mid
        else:
            print(2)
            r = mid - 1
    print(3, l)

solve()