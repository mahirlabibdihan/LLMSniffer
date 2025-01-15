# Good prefixes

from sys import stdin
from math import ceil

for _ in range(int(stdin.readline().strip())) :
    s,n = stdin.readline().split()
    n = int(n)
    score       = 0
    arr         = []

    for ch in s :
        if ch == 'a' :
            score += 1
        else :
            score -= 1
        arr.append(score)
    single = arr[-1]
    # print(arr)

    # Cases
    if single == 0 :
        positives   = 0
        for i in arr :
            if i > 0 :
                positives += 1
        print(n*positives)
    elif single < 0 :
        rounds_positive = []
        for i in arr :
            if i > 0:
                num = ceil(i/(-single))
                if num > n :
                    num = n
            else :
                num = 0
            rounds_positive.append(num)
        # print(rounds_positive)
        print(sum(rounds_positive))
    else :
        rounds_positive = []
        for i in arr :
            if i > 0 :
                num = n
            else :
                num = n - 1 - (-i)//single
                if num < 0 :
                    num = 0
            rounds_positive.append(num)
        # print(rounds_positive)
        print(sum(rounds_positive))
