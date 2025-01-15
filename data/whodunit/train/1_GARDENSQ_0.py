def solve(A, N, M):
    ans = 0
    for i in range(0, N-1):
        for j in range(0, M-1):
            delta, ch = 1, A[i][j]
            while (i + delta) < N and (j + delta) < M:
                if A[i][j + delta] == ch and A[i + delta][j] == ch and A[i + delta][j + delta] == ch:
                    ans += 1
                delta += 1
    print(ans)

if __name__ == '__main__':
    T = (int)(input())
    for _ in range(T):
        N, M = map(int, input().split())
        A = []
        for i in range(N):
            row = input()
            A.append(row)
        solve(A, N, M)
