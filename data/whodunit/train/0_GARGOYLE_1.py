def max_truth_speakers(N, statements):
    truth_speakers = [0]*N
    for statement in statements:
        for i in range(N):
            if statement[i] == 'T':
                truth_speakers[i] += 1
    max_truth = max(truth_speakers)
    return truth_speakers.count(max_truth)

N = int(input())
statements = [list(input()) for _ in range(N)]
print(max_truth_speakers(N, statements))