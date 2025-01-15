T = int(input())
for _ in range(T):
    S = input().strip()
    print(min(S.count('DU'), S.count('UD')))