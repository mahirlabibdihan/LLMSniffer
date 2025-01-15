def check_string(S):
    for char in "LTIME":
        if S.count(char) < 2:
            return "NO"
    return "YES"

T = int(input())
for _ in range(T):
    S = input()
    print(check_string(S))