def max_score(T, test_cases):
    for _ in range(T):
        N, board, points = test_cases[_]
        word = "IITMANDI"
        dp = [0]*(N+1)
        for i in range(1, N+1):
            dp[i] = max(dp[i], dp[i-1])
            score = 0
            word_score = 0
            double_word = 1
            triple_word = 1
            for j in range(8):
                if i-j-1 < 0:
                    break
                if board[i-j-1] == 'd':
                    score += 2*points[j]
                elif board[i-j-1] == 't':
                    score += 3*points[j]
                elif board[i-j-1] == 'D':
                    score += points[j]
                    double_word *= 2
                elif board[i-j-1] == 'T':
                    score += points[j]
                    triple_word *= 3
                else:
                    score += points[j]
                word_score = max(word_score, score*double_word*triple_word)
            dp[i] = max(dp[i], dp[i-8]+word_score)
        print(dp[N])

T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    board = input()
    points = list(map(int, input().split()))
    test_cases.append((N, board, points))
max_score(T, test_cases)