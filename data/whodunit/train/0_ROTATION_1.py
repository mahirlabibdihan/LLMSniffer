def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    offset = 0
    for _ in range(m):
        query = input().split()
        if query[0] == 'C':
            offset = (offset + int(query[1])) % n
        elif query[0] == 'A':
            offset = (offset - int(query[1])) % n
        else:
            print(a[(offset + int(query[1]) - 1) % n])

solve()