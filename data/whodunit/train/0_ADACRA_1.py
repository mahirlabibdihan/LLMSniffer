T = int(input())
for _ in range(T):
    S = input().strip()
    flips = 0
    for i in range(1, len(S)):
        if S[i] != S[i-1]:
            flips += 1
    print(flips)