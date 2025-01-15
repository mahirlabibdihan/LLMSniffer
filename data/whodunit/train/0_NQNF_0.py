import sys
from typing import List, Tuple

def process_queries(n: int, q: int, a: List[int], b: List[int], queries: List[Tuple[int, ...]]) -> List[int]:
    res = []
    for query in queries:
        if query[0] == 1:
            res.append(max(a[query[1]-1:query[2]]))
        elif query[0] == 2:
            for i in range(query[1]-1, query[2]):
                a[i] += b[i]
        elif query[0] == 3:
            for i in range(query[1]-1, query[2]):
                b[i] += query[3]
        elif query[0] == 4:
            for i in range(query[1]-1, query[2]):
                a[i] += query[3]
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