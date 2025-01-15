T = int(input())
for _ in range(T):
    S = list(input())
    i = 0
    while i < len(S) - 3:
        if S[i:i+4] == ['?']*4:
            S[i:i+4] = list('CHEF')
            i += 4
        elif S[i] == '?':
            S[i] = 'A'
            i += 1
        else:
            i += 1
    S = ''.join(S).replace('?', 'A')
    print(S)