T = int(input())
for _ in range(T):
    S = input()
    if S.count('L') >= 2 and S.count('T') >= 2 and S.count('I') >= 2 and S.count('M') >= 2 and S.count('E') >= 2:
        print("YES")
    else:
        print("NO")