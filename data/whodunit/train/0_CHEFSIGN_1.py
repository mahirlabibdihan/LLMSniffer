def min_possible_P(s):
    s = s.split('=')
    max_len = 0
    for i in s:
        if len(i) > max_len:
            max_len = len(i)
    if '>' in s and '<' in s:
        return max_len + 2
    else:
        return 1

T = int(input())
for _ in range(T):
    s = input()
    print(min_possible_P(s))