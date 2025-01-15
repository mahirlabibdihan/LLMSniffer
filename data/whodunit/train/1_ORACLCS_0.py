t = int(input())

for _ in range(t):
    mat = []
    n = int(input())
    na = 1e9
    nb = 1e9
    for _ in range(n):
        s = input()
        na = min(na, s.count('a'))
        nb = min(nb, s.count('b'))
    print(min(na, nb))