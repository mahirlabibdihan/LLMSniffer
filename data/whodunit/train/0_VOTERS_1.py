from collections import defaultdict

def find_common_voters():
    n1, n2, n3 = map(int, input().split())
    voters = defaultdict(int)
    for _ in range(n1+n2+n3):
        voters[int(input())] += 1
    common_voters = [voter for voter, count in voters.items() if count > 1]
    common_voters.sort()
    print(len(common_voters))
    for voter in common_voters:
        print(voter)

find_common_voters()