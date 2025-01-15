T = int(input())
for _ in range(T):
    N = int(input())
    S = list(input())
    min_char = min(S)
    S.remove(min_char)
    S = [min_char] + S
    print(''.join(S))