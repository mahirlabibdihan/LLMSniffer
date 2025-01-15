def solve():
    n = int(input())
    b = [0] * (n + 1)
    a = list(map(int, input().split()))
    free_slot = 1
    ans = 0
    for x in a:
        if 1 <= x <= n:
            if b[x]:
                ans += 1
            else:
                b[x] = 1
        else:
            ans += 1
        pass
    return ans
    pass


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        print(solve())
    pass
