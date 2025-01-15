def max_truth_speakers(N, statements):
    truth_speakers = [0]*N
    for i in range(N):
        for j in range(N):
            if statements[i][j] == 'T':
                truth_speakers[j] += 1
    max_truth = max(truth_speakers)
    return truth_speakers.count(max_truth)

N = int(input())
statements = []
for _ in range(N):
    statement = list(input())
    statements.append(statement)
print(max_truth_speakers(N, statements))