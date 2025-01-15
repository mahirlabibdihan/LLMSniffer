from itertools import combinations

def solve():
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        sets = []
        for _ in range(N):
            set_elements = list(map(int, input().split()))[1:]
            sets.append(set(set_elements))
        count = 0
        for pair in combinations(sets, 2):
            if len(set.union(*pair)) == K:
                count += 1
        print(count)

solve()