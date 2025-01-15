T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    U = input()
    score = 0
    i = 0
    while i < N:
        if U[i] == 'N':
            i += 1
        elif U[i] == S[i]:
            score += 1
            i += 1
        else:
            i += 2
    print(score)