import sys
from typing import List, Tuple

def process_queries(n: int, q: int, a: List[int], b: List[int], queries: List[Tuple[int, ...]]) -> List[int]:
    res = []
    for query in queries:
        t, l, r, *x = query
        l -= 1
        if t == 1:
            res.append(max(a[l:r]))
        elif t == 2:
            a[l:r] = [ai+bi for ai, bi in zip(a[l:r], b[l:r])]
        elif t == 3:
            b[l:r] = [bi+x[0] for bi in b[l:r]]
        elif t == 4:
            a[l:r] = [ai+x[0] for ai in a[l:r]]
    return res

def main():
    n, q = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    queries = [tuple(map(int, sys.stdin.readline().split())) for _ in range(q)]
    res = process_queries(n, q, a, b, queries)
    for r in res:
        print(r)

if __name__ == "__main__":
    main()