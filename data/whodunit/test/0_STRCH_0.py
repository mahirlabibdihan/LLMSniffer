T = int(input())
for _ in range(T):
    N = int(input())
    S, X = input().split()
    S = list(S)
    total = 0
    for i in range(N):
        if S[i] == X:
            total += (i+1)*(N-i)
    print(total)