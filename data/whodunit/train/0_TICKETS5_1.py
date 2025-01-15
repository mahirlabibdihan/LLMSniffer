T = int(input())
for _ in range(T):
    S = input().strip()
    if len(set(S)) != 2:
        print("NO")
    else:
        S = ''.join(sorted(S))
        if S[0] == S[1] and S[1::2] == S[2::2]:
            print("YES")
        else:
            print("NO")