T = int(input())
for _ in range(T):
    N = int(input())
    S = list(input().split())
    if 'cookie' in S and (S[-1] == 'cookie' or 'cookie milk' not in ' '.join(S)):
        print('NO')
    else:
        print('YES')