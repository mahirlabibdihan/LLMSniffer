def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        scores = []
        for i in range(N):
            cookies = list(map(int, input().split()))[1:]
            types = len(set(cookies))
            score = len(cookies)
            if types >= 4:
                score += min(types//4, 1)
            if types >= 5:
                score += min(types//5, 2)
            if types >= 6:
                score += min(types//6, 4)
            scores.append(score)
        max_score = max(scores)
        if scores.count(max_score) > 1:
            print("tie")
        elif scores[0] == max_score:
            print("chef")
        else:
            print(scores.index(max_score) + 1)

solve()