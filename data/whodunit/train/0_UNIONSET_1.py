def solve():
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        sets = [0]*N
        for i in range(N):
            sets[i] = set(map(int, input().split()[1:]))
        count = 0
        for i in range(N):
            for j in range(i+1, N):
                if len(sets[i].union(sets[j])) == K:
                    count += 1
        print(count)

solve()