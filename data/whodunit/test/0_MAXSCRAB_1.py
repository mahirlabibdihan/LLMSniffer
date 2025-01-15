def max_score(T, test_cases):
    for _ in range(T):
        N, board, points = test_cases[_]
        word = "IITMANDI"
        dp = [0]*(N+1)
        for i in range(1, N+1):
            dp[i] = max(dp[i], dp[i-1])
            for j in range(min(i, 8)):
                score = 0
                double_word = 1
                triple_word = 1
                for k in range(j+1):
                    if board[i-k-1] == 'd':
                        score += 2*points[j-k]
                    elif board[i-k-1] == 't':
                        score += 3*points[j-k]
                    elif board[i-k-1] == 'D':
                        score += points[j-k]
                        double_word *= 2
                    elif board[i-k-1] == 'T':
                        score += points[j-k]
                        triple_word *= 3
                    else:
                        score += points[j-k]
                dp[i] = max(dp[i], dp[i-j-1]+score*double_word*triple_word)
        print(dp[N])

T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    board = input()
    points = list(map(int, input().split()))
    test_cases.append((N, board, points))
max_score(T, test_cases)