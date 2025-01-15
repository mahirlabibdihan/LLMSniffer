T = int(input())
for _ in range(T):
    N, M, X, Y = map(int, input().split())
    N -= 1
    M -= 1
    if (N%X == 0 and M%Y == 0 and N//X == M//Y) or (N%X <= 1 and M%Y <= 1 and (N//X == M//Y or N//X+1 == M//Y or N//X == M//Y+1)):
        print("Chefirnemo")
    else:
        print("Pofik")