def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        scores = []
        for i in range(N):
            cookies = list(map(int, input().split()))[1:]
            types = len(set(cookies))
            score = len(cookies)
            if types == 4:
                score += 1
            elif types == 5:
                score += 2
            elif types == 6:
                score += 4
            scores.append(score)
        max_score = max(scores)
        winners = [i for i, score in enumerate(scores) if score == max_score]
        if len(winners) > 1:
            print("tie")
        elif winners[0] == 0:
            print("chef")
        else:
            print(winners[0] + 1)

solve()