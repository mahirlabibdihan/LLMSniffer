
try:
    from itertools import combinations
    for _ in range(int(input())):
        scores = list(map(int, input().split()))
        k = int(input())
        s = combinations(scores, k)
        res = []
        for i in s:
            res.append(sum(i))
        print(res.count(max(res)))
except EOFError:
    pass

    
