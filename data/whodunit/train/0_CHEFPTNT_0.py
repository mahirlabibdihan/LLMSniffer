T = int(input())
for _ in range(T):
    N, M, X, K = map(int, input().split())
    S = input()
    E = S.count('E')
    O = S.count('O')
    for i in range(1, M+1):
        if i%2 == 0:
            work = min(E, X)
            E -= work
        else:
            work = min(O, X)
            O -= work
        N -= work
    if N <= 0:
        print("yes")
    else:
        print("no")