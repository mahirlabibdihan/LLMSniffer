from collections import Counter

def find_common_voters():
    n1, n2, n3 = map(int, input().split())
    voters = []
    for _ in range(n1+n2+n3):
        voters.append(int(input()))
    common_voters = [item for item, count in Counter(voters).items() if count > 1]
    common_voters.sort()
    print(len(common_voters))
    for voter in common_voters:
        print(voter)

find_common_voters()