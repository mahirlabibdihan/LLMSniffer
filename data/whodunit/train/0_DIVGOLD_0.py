T = int(input())
for _ in range(T):
    N = int(input())
    S = list(input())
    min_char = min(S)
    min_index = S.index(min_char)
    S.remove(min_char)
    S.insert(0, min_char)
    print(''.join(S))