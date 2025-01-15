def correct_score(T, votes):
    for _ in range(T):
        N = votes[_][0]
        vote_list = votes[_][1]
        vote_dict = {}
        for vote in vote_list:
            user, vote_type = vote.split()
            vote_dict[user] = vote_type
        print(sum(1 if vote_type == '+' else -1 for vote_type in vote_dict.values()))

T = int(input())
votes = []
for _ in range(T):
    N = int(input())
    vote_list = [input() for _ in range(N)]
    votes.append((N, vote_list))
correct_score(T, votes)