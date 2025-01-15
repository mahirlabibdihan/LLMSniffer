T = int(input())
for _ in range(T):
    N = int(input())
    correct_answers = input()
    chef_answers = input()
    winnings = list(map(int, input().split()))
    correct_count = sum([correct_answers[i] == chef_answers[i] for i in range(N)])
    if correct_count == N:
        print(winnings[N])
    else:
        print(max(winnings[:correct_count+1]))