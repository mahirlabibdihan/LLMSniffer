T = int(input())
for _ in range(T):
    N, M, X, K = map(int, input().split())
    S = input()
    E = S.count('E')
    O = S.count('O')
    for i in range(1, M+1):
        if i%2 == 0:
            if E > X:
                N -= X
                E -= X
            else:
                N -= E
                E = 0
        else:
            if O > X:
                N -= X
                O -= X
            else:
                N -= O
                O = 0
    if N <= 0:
        print("yes")
    else:
        print("no")