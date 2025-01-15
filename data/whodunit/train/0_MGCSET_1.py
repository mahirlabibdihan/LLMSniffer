from sys import stdin, stdout
from itertools import chain, combinations

def good_subsequences(T, nm_list, a_list):
    for _ in range(T):
        n, m = nm_list[_]
        a = a_list[_]
        count = 0
        comb = chain(*map(lambda x: combinations(a, x), range(0, len(a) + 1)))
        for c in list(comb):
            if sum(c) % m == 0:
                count += 1
        stdout.write(str(count) + "\n")

T = int(stdin.readline())
nm_list = []
a_list = []
for _ in range(T):
    n, m = map(int, stdin.readline().split())
    nm_list.append((n, m))
    a = list(map(int, stdin.readline().split()))
    a_list.append(a)
good_subsequences(T, nm_list, a_list)