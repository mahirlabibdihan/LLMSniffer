def solve():
    T = int(input())
    for _ in range(T):
        k, s = input().split()
        k = int(k)
        n = 1 << k
        s = list(s)
        for i in range(n):
            j = int("{:0{width}b}".format(i, width=k)[::-1], 2)
            if i < j:
                s[i], s[j] = s[j], s[i]
        print(''.join(s))

solve()