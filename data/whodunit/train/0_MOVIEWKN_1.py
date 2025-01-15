T = int(input())
for _ in range(T):
    n = int(input())
    L = list(map(int, input().split()))
    R = list(map(int, input().split()))
    movies = sorted([(L[i]*R[i], R[i], -i) for i in range(n)], reverse=True)
    print(-movies[0][2] + 1)