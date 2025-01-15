T = int(input())
for _ in range(T):
    N = int(input())
    S = list(input().split())
    flag = 0
    for i in range(N-1):
        if S[i] == 'cookie' and S[i+1] != 'milk':
            flag = 1
            break
    if S[-1] == 'cookie':
        flag = 1
    if flag == 0:
        print('YES')
    else:
        print('NO')