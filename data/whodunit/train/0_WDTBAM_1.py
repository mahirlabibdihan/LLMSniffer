def max_winnings(T, data):
    for t in range(T):
        N = data[t][0]
        correct_answers = data[t][1]
        chef_answers = data[t][2]
        winnings = data[t][3]
        correct_count = sum([correct_answers[i] == chef_answers[i] for i in range(N)])
        if correct_count == N:
            print(winnings[N])
        else:
            print(max(winnings[:correct_count+1]))

T = int(input())
data = []
for _ in range(T):
    N = int(input())
    correct_answers = input()
    chef_answers = input()
    winnings = list(map(int, input().split()))
    data.append((N, correct_answers, chef_answers, winnings))
max_winnings(T, data)