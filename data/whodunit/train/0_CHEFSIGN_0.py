def min_possible_P(s):
    if '>' not in s and '=' in s:
        return 1
    if '<' not in s and '=' in s:
        return 1
    if '<' not in s and '>' in s:
        return 2
    s = s.split('=')
    max_len = max(len(i) for i in s)
    return max_len + 2

T = int(input())
for _ in range(T):
    s = input()
    print(min_possible_P(s))